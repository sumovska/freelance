#! /usr/bin/env python

######################################################################
#
# Company Confidential. Copyright (c) Cochlear Limited 2012.
#
# $Change: 232759 $
# $Revision: #15 $
# $DateTime: 2014/05/21 17:56:59 $
# Authors: Pawel Plesnar
# References:
#
#######################################################################

"""
IDLC protocol implementation
"""

import logging
import time
import collections
import crcmod
from cochlear.protocols.protocol import ProtocolError, ProtocolTimeout, \
    Protocol


class IdlcError(ProtocolError):
    pass


class IdlcTimeout(ProtocolTimeout):
    pass


class IdlcCrcError(IdlcError):
    pass


class IdlcFrameFlagError(IdlcError):
    pass


class IdlcFrameTypeError(IdlcError):
    pass


class IdlcNegotiationError(IdlcError):
    pass


class Idlc(Protocol):
    '''
    Transceiver for IDLC
    '''
    write_default_keys = {"timeout": 10.0}
    error = IdlcError
    timeout = IdlcTimeout

    FLAG = 0x7e
    ESCAPE = 0x7d
    ESCAPELIST = [FLAG, ESCAPE]
    SNRM = 0x93
    UA = 0x73
    DISC = 0x53
    DM = 0x1f

    CRC_POLYNOMIAL = 0x11021
    CRC_INITIAL = 0xFFFF

    # Link timeout table (in seconds)
    link_timeout_table = {
        0x01: 0.040,
        0x02: 0.080,
        0x04: 0.160,
        0x08: 0.320,
        0x10: 0.640,
        0x20: 1.280,
        0x40: 2.560,
        0x80: 5.120,
    }

    max_tx_data_bytes = 0xffff

    max_rx_data_bytes = 0xffff

    link_timeout_setting = 0xf0

    link_establishment_timeout = link_timeout_table[0x10]

    retries = 3

    data_timeout = 1

    auto_connect = True

    ignore_frame_errors = False

    ignore_crc_errors = False

    verbose = 0

    transmitDelay = 0

    def __init__(self, tag, lower, timeout_override=None):
        '''
        @param tag: tag for logging purposes
        @param lower: lower protocol layer
        @param timeout_override: overrides the timeout received from the device with a custom value
        '''
        Protocol.__init__(self, tag, lower=lower)
        self.clear()
        self.timeout_override = timeout_override

    def connect(self):
        '''
        Establishes connection with device
        '''
        Protocol.connect(self)
        self._connect()

    def is_connected(self):
        '''
        Test if connection is established
        '''
        return self.connected

    def write(self, **keys):
        '''
        Writes data to the IDLC
        keys: data - data to be sent

        @raise IdlcError: if IDLC is not connected
        '''
        keys = Protocol.write(self, **keys)
        data = keys["data"]

        if self._logger.isEnabledFor(logging.DEBUG):
            self._logger.debug("Sent data: "
                               + str([hex(x) for x in data]))
        if not self.is_connected():
            raise self.error("IDLC not connected: call connect()")
        self._sendBytes(keys)

    def read(self, **keys):
        '''
        Processes message for the upper layer
        keys: timeout
        return keys: data
        '''
        keys = Protocol.read(self, **keys)

        return_keys = self._getBytes(keys)

        if self._logger.isEnabledFor(logging.DEBUG):
            self._logger.debug("Received data: "
                               + str([hex(x) for x in return_keys["data"]]))

        return return_keys

    def disconnect(self):
        '''
        Close IDLC connection
        '''
        self._disconnect()

    def clear(self):
        '''
        Clears the protocol
        @note: connection is reestablished
        '''
        Protocol.disconnect(self)
        Protocol.connect(self)
        self.reset()
        self.tx_frame_buffer = collections.deque()
        self.rx_frame_buffer = collections.deque()
        self.rx_buffer_keys = {}
        self.buffer_keys = {}
        self.buffer = collections.deque()

    def reset(self):
        '''
        Reset the IDLC state machine, without sending anything to the slave.
        '''
        self.connected = False
        self.nR = 0
        self.nS = 0

    def _raiseError(self, ErrorClass):
        '''
        Raises an error with additionally clearing the protocol
        '''
        self.clear()
        raise ErrorClass(self)

    def _setTimeout(self, link_timeout):
        '''
        Sets the timeouts (for internal use only)
        '''
        self.link_timeout = link_timeout
        self.retry_timeout = float(link_timeout) / (self.retries + 1)
        self._lower.set_timeout(self.retry_timeout)

    def _sendFrame(self, keys):
        '''
        Send an IDLC frame.

        This method will do byte stuffing and add flags and a CRC.
        '''
        data = keys["data"]
        transmit_delay = keys.get("idlc_transmit_delay")
        if transmit_delay is not None:
            time.sleep(transmit_delay)
        frame = []
        frame.append(self.FLAG)
        c = crcmod.Crc(self.CRC_POLYNOMIAL, initCrc=self.CRC_INITIAL, rev=False)
        c.update("".join(chr(x) for x in data))
        c = c.crcValue
        data.append(c >> 8)
        data.append(c & 0xff)
        for i in data:
            if i in self.ESCAPELIST:
                frame.append(self.ESCAPE)
                i = i ^ 0x20
            frame.append(i)
        frame.append(self.FLAG)

        keys["data"] = frame
        self._write_lower(keys)

    def _getFrame(self, keys):
        '''
        Receive an IDLC frame

        This method will do byte unstuffing and checks the CRC.
        '''
        timeout = keys["timeout"]
        start_time = time.time()
        end_time = start_time + timeout
        time_left = timeout

        while 1:
            return_keys = {}

            time_left = max(end_time - time.time(), 0)
            keys["timeout"] = time_left
            return_keys = self._buffer_read(keys)

            b = return_keys["data"]
            if b == self.FLAG:
                break
            else:
                if not self.ignore_frame_errors:
                    self._raiseError(IdlcFrameFlagError)
                else:
                    return_keys["data"] = []
                    return return_keys
        data = []
        c = crcmod.Crc(self.CRC_POLYNOMIAL, initCrc=self.CRC_INITIAL, rev=False)
        while 1:
            time_left = max(end_time - time.time(), 0)
            keys["timeout"] = time_left
            b = self._buffer_read(keys)["data"]
            if b == self.FLAG:
                if data:
                    break
            if b == self.ESCAPE:
                time_left = max(end_time - time.time(), 0)
                keys["timeout"] = time_left
                b = self._buffer_read(keys)["data"]
                b = b ^ 0x20
            c.update(chr(b))
            data.append(b)
        if c.crcValue != 0:
            if not self.ignore_crc_errors:
                self._raiseError(IdlcCrcError)
            else:
                return_keys["data"] = []
                return return_keys
        return_keys["data"] = data[:-2]
        return return_keys

    def _sendSnrm(self, keys):
        '''
        Send an SNRM frame
        '''
        self._logger.debug("Sending SNRM frame")
        keys["data"] = [self.SNRM, self.link_timeout_setting,
                        self.max_rx_data_bytes >> 8, self.max_rx_data_bytes & 0xff]
        self._sendFrame(keys)

    def _sendDisc(self, keys):
        '''
        Send a Disc frame
        '''
        self._logger.debug("Sending DISC frame")
        keys["data"] = [self.DISC]
        self._sendFrame(keys)

    def _sendI(self, keys):
        '''
        Send an I frame
        '''
        if "data" in keys:
            data = keys["data"]
        else:
            data = []
        if self._logger.isEnabledFor(logging.DEBUG):
            self._logger.debug("Sending I frame: NS=%d NR=%d DATA=%d bytes",
                               self.nS,
                               self.nR,
                               len(data))
        ctrl = (self.nR << 5) + (1 << 4) + (self.nS << 1)
        keys["data"] = [ctrl] + data
        self._sendFrame(keys)

    def _getI(self, keys):
        '''
        Get an I frame
        '''
        self._lower.time1 = time.time()
        return_keys = self._getFrame(keys)
        data = return_keys["data"]
        self._logger.debug("Receiving I frame")

        if data:
            ctrl = data[0]
            nR = ctrl >> 5
            nS = (ctrl >> 1) & 0x07
            if (ctrl & 0x01) == 0:
                self._logger.debug(">NR=%d NS=%d DATA=%d bytes",
                                   nR, nS, len(data) - 1)
                if nS == self.nR:
                    # We were expecting this frame, accept the data
                    self.nR = (self.nR + 1) % 8
                    self.rx_frame_buffer.extend(data[1:])
                    self.rx_buffer_keys = return_keys
                else:
                    self._logger.debug(">NR=%d got nS = %d",
                                       self.nR, nS)
                if nR == (self.nS + 1) % 8:
                    self.nS = (self.nS + 1) % 8
                    self.tx_frame_buffer.clear()
                else:
                    self._logger.debug(">NS=%d got nR = %d",
                                       self.nS, nR)
            else:
                if ctrl == self.DM:
                    self._logger.debug(">Received DM frame")
                    self.reset()
                    if self.auto_connect:
                        self.connect()
                    else:
                        self._raiseError(IdlcError)
                else:
                    self._raiseError(IdlcFrameTypeError)

    def _buffer_read(self, keys):
        '''
        Read buffered data
        '''
        if not self.buffer:
            return_keys = self._read_lower(keys)
            self.buffer.extend(return_keys["data"])
            self.buffer_keys = return_keys
        return_keys = self.buffer_keys
        return_keys["data"] = self.buffer.popleft()
        return return_keys

    def _connect(self):
        '''
        Connect the link
        '''
        # Here buffers must not be cleared, because connect is called from
        # withing the sendBytes/getBytes.
        self.reset()
        self._setTimeout(self.link_establishment_timeout)
        keys = {"timeout": self.retry_timeout}
        retries_left = self.retries
        while not self.connected:
            try:
                self._sendSnrm(dict(keys))
                data = self._getFrame(keys)["data"]
                if not data:
                    self._raiseError(IdlcError)
                if data[0] == self.UA:
                    self._logger.debug("Received UA frame")
                    self.connected = True
                    if len(data) >= 2:
                        if self.timeout_override is None:
                            timeout_setting = self.link_timeout_setting & data[1]
                            if timeout_setting not in self.link_timeout_table:
                                self._raiseError(IdlcNegotiationError)
                            link_timeout = self.link_timeout_table[timeout_setting]
                        else:
                            link_timeout = self.timeout_override
                        self._setTimeout(link_timeout)
                        keys["timeout"] = self.retry_timeout
                    if len(data) >= 4:
                        self.max_tx_data_bytes = min(self.max_tx_data_bytes,
                                                     (data[2] << 8) + data[3])
                        self._logger.debug("max TX bytes = %d",
                                           self.max_tx_data_bytes)
                elif data[0] == self.DM:
                    self._raiseError(IdlcError)
                else:
                    self._raiseError(IdlcFrameTypeError)
            except (ProtocolTimeout, ProtocolError) as e:
                self._logger.debug("Exception in connect: %s" % e)
                self._logger.debug("Retries_left: %d" % retries_left)
                if not retries_left:
                    self._raiseError(IdlcError)
                retries_left -= 1

    def _disconnect(self):
        '''
        Disconnect the IDLC link.
        '''
        self.clear()
        keys = {"timeout": self.link_establishment_timeout}
        retries_left = self.retries
        while True:
            try:
                self._sendDisc(dict(keys))
                data = self._getFrame(keys)["data"]
                if len(data) == 0:
                    self._raiseError(IdlcError)
                if (data[0] != self.DM) and (data[0] != self.UA):
                    self._raiseError(IdlcFrameTypeError)
                return data[0]
            except (ProtocolTimeout, ProtocolError) as e:
                self._logger.debug("Exception in disconnect: %s" % e)
                self._logger.debug("Retries_left: %d" % retries_left)
                if not retries_left:
                    self._raiseError(IdlcError)
                retries_left -= 1

    def _sendBytes(self, keys):
        '''
        Send bytes reliably to the other side.
        '''
        if not self.connected and self.auto_connect:
            self.connect()
        retries_left = self.retries
        data = keys["data"]
        timeout = keys["timeout"]
        if timeout <= 0:
            raise self.error("IDLC needs a timeout > 0")
        start_time = time.time()
        end_time = start_time + timeout
        time_left = timeout
        while data or self.tx_frame_buffer:
            if not time_left:
                self._raiseError(IdlcTimeout)
            if not self.tx_frame_buffer:
                n = min(len(data), self.max_tx_data_bytes)
                self.tx_frame_buffer.extend(data[:n])
                data = data[n:]
            try:
                time_left = max(end_time - time.time(), 0)
                self._sendI({"data": list(self.tx_frame_buffer),
                             "timeout": time_left})
                time_left = max(end_time - time.time(), 0)
                self._getI({"timeout": time_left})

                retries_left = self.retries
            except (ProtocolTimeout, ProtocolError) as e:
                self._logger.debug("Exception in sendBytes: %s" % e)
                self._logger.debug("Retries_left: %d" % retries_left)
                if not retries_left:
                    self._raiseError(IdlcError)
                retries_left -= 1

    def _getBytes(self, keys):
        '''
        Get bytes reliably from the other side.
        '''
        if not self.connected and self.auto_connect:
            self.connect()
        timeout = keys["timeout"]
        if timeout <= 0:
            raise self.error("IDLC needs a timeout > 0")
        retries_left = self.retries
        start_time = time.time()
        end_time = start_time + timeout
        time_left = timeout
        while not self.rx_frame_buffer:
            if not time_left:
                self._raiseError(IdlcTimeout)
            try:
                time_left = max(end_time - time.time(), 0)
                keys["timeout"] = time_left
                self._sendI(dict(keys))

                time_left = max(end_time - time.time(), 0)
                keys["timeout"] = time_left
                self._getI(keys)

                retries_left = self.retries
            except (ProtocolTimeout, ProtocolError) as e:
                self._logger.debug("Exception in getBytes: %s" % e)
                self._logger.debug("Retries_left: %d" % retries_left)
                if not retries_left:
                    self._raiseError(IdlcError)
                retries_left -= 1
        return_keys = self.rx_buffer_keys
        return_keys["data"] = list(self.rx_frame_buffer)
        self.rx_frame_buffer.clear()
        return return_keys
