from enum import Enum


class ThreadStateEnum(Enum):
    NULL = 0
    ONLINE = 1
    STOPPED = 2
    ERROR = 3
    EXIT = 4
