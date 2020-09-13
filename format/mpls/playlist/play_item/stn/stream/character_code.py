from aenum import Enum


class CharacterCode(Enum):
    UTF_8 = 0x01
    UTF_16BE = 0x02
    SHIFT_JIS = 0x03
    KSC5601_INCL_KSC5653 = 0x04
    GB18030_2000 = 0x05
    GB2312 = 0x06
    BIG5 = 0x07
