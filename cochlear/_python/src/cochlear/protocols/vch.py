#! /usr/bin/env python

######################################################################
#
# Company Confidential. Copyright (c) Cochlear Limited 2012.
#
# $Change: 232759 $
# $Revision: #5 $
# $DateTime: 2014/05/21 17:56:59 $
# Authors: Pawel Plesnar
# References:
#
#######################################################################

"""
VCH protocol implementation
"""

import collections
import threading
import time
from Queue import Queue, Empty
from cochlear.protocols.protocol import ProtocolError, ProtocolTimeout, \
    Protocol

VCH_FRAME_SOH = 1
VCH_FRAME_EOT = 4


class VchError(ProtocolError):
    pass


class VchTimeout(ProtocolTimeout):
    pass


class Vch(Protocol, threading.Thread):
    '''
    Protocol class for VCH protocol
    -Can buffer messages for separate channels
    -Can run a thread to fill buffers with data by itself (TODO)
    -Write must be provided with the following keys:
        data -> list of bytes that will be attached to the VCH frame
        vch_channel -> The VCH channel for the frame
    -Read must be provided with following keys:
        vch_channel -> The VCH channel of the received frame

    '''
    write_needed_keys = ["data", "vch_channel"]
    read_needed_keys = ["vch_channel"]
    error = VchError
    timeout = VchTimeout

    HEADER_SIZE = 4
    END_SIZE = 1
    OVERHEAD_SIZE = HEADER_SIZE + END_SIZE

    def __init__(self, tag=None, lower=None, buffer_channels=False,
                 max_size=None, threaded=False):
        Protocol.__init__(self, tag, lower)
        threading.Thread.__init__(self)
        self._data_buffer = collections.deque()
        if buffer_channels:
            self._channel_buffers = {}
        else:
            self._channel_buffers = None

        if self._lower is not None and self._lower.payload_size is not None:
            if max_size is not None:
                if self._lower.payload_size < max_size:
                    raise self.error("Lower layer has insufficient payload size")
                else:
                    self.payload_size = max_size - self.OVERHEAD_SIZE
            else:
                self.payload_size = self._lower.payload_size - self.OVERHEAD_SIZE
        elif max_size is not None:
            self.payload_size = max_size - self.OVERHEAD_SIZE
        else:
            self.payload_size = None
        self.threaded = threaded
        if threaded:
            self.buffer_lock = threading.Lock()
            self.stop_thread = threading.Event()
            self.daemon = True
            self.start()

    def write(self, **keys):
        '''
        Send VCH frame to the lower layer
            keys used: data, vch_channel
        '''
        keys = Protocol.write(self, **keys)

        data = keys["data"]
        vch_channel = keys.pop("vch_channel")

        data = ([VCH_FRAME_SOH, 0, 0, vch_channel]
                + data
                + [VCH_FRAME_EOT])
        data[1] = len(data) >> 8
        data[2] = len(data) & 0xFF

        self._logger.debug("Sending frame (" + str(len(data)) + " bytes)")

        keys["data"] = data
        self._write_lower(keys)

    def read(self, **keys):
        '''
        Processes message for the upper layer
            return keys: data, vch_channel
        '''
        keys = Protocol.read(self, **keys)
        vch_timeout = keys["timeout"]
        vch_channel = keys.pop("vch_channel")

        self._logger.debug("Receiving frame)")

        if self.threaded:
            self.buffer_lock.acquire()
        if self._channel_buffers is not None:
            if vch_channel not in self._channel_buffers:
                self._channel_buffers[vch_channel] = Queue()
            selected_buffer = self._channel_buffers[vch_channel]
            if self.threaded:
                self.buffer_lock.release()
                try:
                    return selected_buffer.get(True, vch_timeout)
                except Empty:
                    raise VchTimeout
            else:
                try:
                    return selected_buffer.get(False)
                except Empty:
                    pass

        start_time = time.time()
        end_time = start_time + vch_timeout
        time_left = 1
        while time_left:
            return_keys = {}
            i = 0
            vch_length = 0
            vch_channel_received = 0
            vch_data = []

            while time_left:
                time_left = max(end_time - time.time(), 0)
                keys["timeout"] = time_left
                if not self._data_buffer:
                    try:
                        return_keys.update(self._read_lower(keys))
                    except ProtocolTimeout:
                        continue
                    self._data_buffer.extend(return_keys["data"])
                if i == 0:
                    if self._data_buffer.popleft() == VCH_FRAME_SOH:
                        i += 1
                elif i == 1:
                    vch_length = self._data_buffer.popleft() << 8
                    i += 1
                elif i == 2:
                    vch_length += self._data_buffer.popleft()
                    i += 1
                elif i == 3:
                    vch_channel_received += self._data_buffer.popleft()
                    i += 1
                elif i >= vch_length - 1:
                    if self._data_buffer.popleft() != VCH_FRAME_EOT:
                        raise self.error("Vch EOT not received")
                    self._data_buffer.clear()
                    break
                else:
                    data_to_read = min(len(self._data_buffer),
                                       vch_length - i - 1)
                    for _ in range(data_to_read):
                        vch_data.append(self._data_buffer.popleft())
                    i += data_to_read
            self._data_buffer.clear()

            return_keys["data"] = vch_data
            return_keys["vch_channel"] = vch_channel_received

            if i >= 4:
                if self._channel_buffers is not None:
                    if vch_channel_received == vch_channel:
                        break
                    else:
                        if vch_channel_received not in self._channel_buffers:
                            self._channel_buffers[vch_channel_received] = Queue()
                        self._channel_buffers[vch_channel_received].put(return_keys)
                elif vch_channel_received == vch_channel:
                    break
        if vch_timeout and not time_left:
            raise self.timeout
        return return_keys

    def set_lower(self, protocol):
        self._lower = protocol
        if self._lower is not None and self._lower.payload_size is not None:
            self.payload_size = self._lower.payload_size - self.OVERHEAD_SIZE

    def run(self):
        while not self.stop_thread.is_set():
            return_keys = {}
            i = 0
            vch_length = 0
            vch_channel = 0
            vch_data = []
            read_keys = {"timeout": 1}

            while not self.stop_thread.is_set():
                if not self._data_buffer:
                    if self._lower.is_connected():
                        try:
                            return_keys.update(self._read_lower(read_keys))
                        except ProtocolTimeout:
                            continue
                        self._data_buffer.extend(return_keys["data"])
                    else:
                        # TODO: try to reconnect?
                        time.sleep(0.5)
                        continue
                if i == 0:
                    if self._data_buffer.popleft() == VCH_FRAME_SOH:
                        i += 1
                elif i == 1:
                    vch_length = self._data_buffer.popleft() << 8
                    i += 1
                elif i == 2:
                    vch_length += self._data_buffer.popleft()
                    i += 1
                elif i == 3:
                    vch_channel += self._data_buffer.popleft()
                    i += 1
                elif i >= vch_length - 1:
                    if self._data_buffer.popleft() != VCH_FRAME_EOT:
                        raise self.error("Vch EOT not received")
                    self._data_buffer.clear()
                    break
                else:
                    data_to_read = min(len(self._data_buffer),
                                       vch_length - i - 1)
                    for _ in range(data_to_read):
                        vch_data.append(self._data_buffer.popleft())
                    i += data_to_read

            return_keys["data"] = vch_data
            return_keys["vch_channel"] = vch_channel

            with self.buffer_lock:
                if vch_channel not in self._channel_buffers:
                    self._channel_buffers[vch_channel] = Queue()
                self._channel_buffers[vch_channel].put(return_keys)

    def disconnect(self):
        if self.threaded:
            self.stop_thread.set()
            self.join(5)
            if self.is_alive():
                raise VchError("Cannot end receiver thread")
        Protocol.disconnect(self)
