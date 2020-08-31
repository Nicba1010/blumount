from aenum import Enum


class StreamType(Enum):
    RESERVED = 0
    USED_BY_PLAY_ITEM = 1
    USED_BY_SUB_PATH_TYPE_23456 = 2
    USED_BY_SUB_PATH_TYPE_7 = 3
    USED_BY_SUB_PATH_TYPE_10 = 4
