from aenum import Enum


class VideoFormat(Enum):
    FORMAT_480I = 0x01
    FORMAT_576I = 0x02
    FORMAT_480P = 0x03
    FORMAT_1080I = 0x04
    FORMAT_720P = 0x05
    FORMAT_1080P = 0x06
    FORMAT_576P = 0x07
    FORMAT_2160P = 0x08
