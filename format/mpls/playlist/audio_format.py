from aenum import Enum


class AudioFormat(Enum):
    MONO = 0x01
    STEREO = 0x03
    MULTICHANNEL = 0x06
    STEREO_MULTICHANNEL = 0x0C
