from aenum import Enum


class HDMVTitlePlaybackType(Enum):
    """
    Represents the reproduction type of an HDMV title
    """
    TYPE_0 = 0b00
    TYPE_1 = 0b01
    TYPE_2 = 0b10
    TYPE_3 = 0b11
