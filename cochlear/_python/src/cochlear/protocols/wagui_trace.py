#! /usr/bin/env python

"""
WAGUI TRACE protocol implementation
"""

import time
from collections import OrderedDict
from threading import Thread, Lock, Event

from cochlear.protocols.protocol import ProtocolError, ProtocolTimeout, \
    Protocol


class WaguiTraceProtocolError(ProtocolError):
    pass


class WaguiTraceProtocolTimeout(ProtocolTimeout):
    pass


class WaguiTraceProtocol(Protocol, Thread):
    '''
    Protocol class for Wagui Trace
    -This protocol is an automated Thread that constantly polls the
        lower layer protocol for wagui trace data
    -Only the 'get*' and 'wait*' methods should be used to access
        received traces
    '''
    read_default_keys = {"timeout": 1.0}
    error = WaguiTraceProtocolError

    __END_OF_LINE = chr(10)
    __END_OF_FRAME = chr(0)

    __last_screen = None
    __last_overlay = None
    __last_sound = None

    def __init__(self, tag=None, lower=None):
        Thread.__init__(self)
        Protocol.__init__(self, tag, lower)
        self.__wait_screen = Event()
        self.__wait_overlay = Event()
        self.__wait_sound = Event()
        self.__trace_lock = Lock()
        self.__stop_request = Event()
        self.daemon = True
        self.start()

    def write(self, **keys):
        raise WaguiTraceProtocolError("WAGUI trace can only receive")

    def read(self, **keys):
        '''
        Processes message for the upper layer
            return keys: responses
        '''
        keys = Protocol.read(self, **keys)

        self._logger.debug("Receiving trace")

        return_keys = self._read_lower(keys)
        return_keys["data"] = self.__decode_trace(return_keys["data"])
        return return_keys

    def __decode_trace(self, data):
        data = "".join(chr(x) for x in data)
        if not data.endswith(self.__END_OF_FRAME):
            raise WaguiTraceProtocolError("No EOF in trace")
        datas = data.split(self.__END_OF_FRAME)[:-1]
        traces = []
        for data in datas:
            lines = data.split(self.__END_OF_LINE)
            header = lines[0]
            if len(header) != 4:
                raise WaguiTraceProtocolError("Wrong trace header length")
            trace_data = OrderedDict()
            trace_data["header"] = header
            trace_data["timestamp"] = time.time()
            for param in lines[1:]:
                trace_data.update(self.__parseParam(param))
            traces.append(trace_data)
        return traces

    def __parseParam(self, param):
        paramName = param[:2]
        paramHex = param[2:]
        if paramName[1] == ":":
            value = paramHex
        else:
            value = 0
            if(len(paramHex) == 1):
                value = int(paramHex, 16)
            else:
                if(int(paramHex[len(paramHex) - 2], 16) & 0x8):
                    negative = len(paramHex)
                else:
                    negative = 0
                while(len(paramHex) > 0):
                    value = value << 8
                    value += int(paramHex[-2:], 16)
                    paramHex = paramHex[:-2]
                if(negative != 0):
                    '''two's complement'''
                    value -= 1
                    value = ~value
                    value &= int(negative * "f", 16)
                    value *= -1
        return {paramName: value}

    def run(self):
        while not self.__stop_request.is_set():
            try:
                datas = self.read()["data"]
            except ProtocolTimeout:
                pass
            else:
                for data in datas:
                    header = data["header"]
                    with self.__trace_lock:
                        if header.startswith("S"):
                            self.__last_sound = data
                            self.__wait_sound.set()
                        elif header == "Hmon":
                            pass
                        elif header[1] == "O":
                            self.__last_overlay = data
                            self.__wait_overlay.set()
                        else:
                            self.__last_screen = data
                            self.__wait_screen.set()
                    self._logger.info("Trace recieved: "
                                      + str(data))

    def get_last_screen(self):
        with self.__trace_lock:
            ret = self.__last_screen
            self.__wait_screen.clear()
        self._logger.info("Get Screen: "
                          + str(ret))
        return ret

    def get_last_overlay(self):
        with self.__trace_lock:
            ret = self.__last_overlay
            self.__wait_overlay.clear()
        return ret

    def get_last_sound(self):
        with self.__trace_lock:
            ret = self.__last_sound
            self.__wait_sound.clear()
        return ret

    def wait_for_new_screen(self, timeout):
        if self.__wait_screen.wait(timeout):
            ret = self.get_last_screen()
            self._logger.info("Get Screen: "
                              + str(ret))
            return ret
#            return self.get_last_screen()
        return None

    def wait_for_new_overlay(self, timeout):
        if self.__wait_overlay.wait(timeout):
            return self.get_last_overlay()
        return None

    def wait_for_new_sound(self, timeout):
        if self.__wait_sound.wait(timeout):
            return self.get_last_sound()
        return None

    def disconnect(self):
        self.__stop_request.set()
        self.join(5)
        if self.is_alive():
            raise WaguiTraceProtocolError("Cannot end receiver thread")
        Protocol.disconnect(self)
