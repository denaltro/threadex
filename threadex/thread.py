import sys
import time
import logging
import threading
from queue import Queue

from threadex.states import ThreadStateEnum


class Thread(threading.Thread):
    def __init__(self, *args, **kwargs):
        self.method = kwargs.pop('target')
        super(Thread, self).__init__(target=self.run_method, *args, **kwargs)

        self.__state = ThreadStateEnum.NULL
        self.__result = None
        self.__error = None
        self.__queue_result = Queue()

        self.__time_start = None
        self.__time_end = None

    def start(self):
        self.__run_backup = self.run
        self.run = self.__run
        threading.Thread.start(self)
        self.__time_start = time.monotonic()
        self.__state = ThreadStateEnum.ONLINE
        del self

    def stop(self):
        self.__time_end = time.monotonic()
        self.__state = ThreadStateEnum.STOPPED

    def __run(self):
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, event, arg):
        if event == 'call':
            return self.localtrace
        return None

    def localtrace(self, frame, event, arg):
        if self.__state is ThreadStateEnum.STOPPED and event == 'line':
            raise SystemExit()
        return self.localtrace

    def run_method(self, *args, **kwargs):
        try:
            self.__result = self.method(*args, *kwargs)
            self.__queue_result.put(self.__result)
            self.__state = ThreadStateEnum.EXIT
        except Exception as e:
            t, v, tb = sys.exc_info()
            self.__error = e.with_traceback(tb)
            self.__state = ThreadStateEnum.ERROR
        self.__time_end = time.monotonic()

    @property
    def state(self):
        return self.__state

    @property
    def result(self):
        if self.__error:
            raise self.__error
        return self.__queue_result.get()

    @property
    def uptime(self):
        if self.__time_start:
            return self.__time_end if self.__time_end else time.monotonic() - self.__time_start
