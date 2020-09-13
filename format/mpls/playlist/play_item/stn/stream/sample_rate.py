from aenum import Enum


class SampleRate(Enum):
    KHZ_48 = 0x01
    KHZ_96 = 0x04
    KHZ_192 = 0x05
    KHZ_48_192 = 0x0C
    KHZ_48_96 = 0x0E
