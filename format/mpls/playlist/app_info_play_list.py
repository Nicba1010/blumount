from typing import IO

from base import LoggingClass
from base.utils import get_flag
from utils.utils import Endianess, read_u8, read_u16, hex_log_str, read_u32
from .playback_type import PlaybackType
from .u0_mask_table import U0MaskTable


class AppInfoPlayList(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.length: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Length: {self.length}")

        self.reserved_1: bytes = f.read(1)
        self.logger.debug(f"Reserved 1: {hex_log_str(self.reserved_1)}")

        self.playback_type: PlaybackType = PlaybackType(read_u8(f, endianess=Endianess.BIG_ENDIAN))

        if self.playback_type in [PlaybackType.UNKNOWN_1, PlaybackType.UNKNOWN_2]:
            self.playback_count: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
            self.logger.debug(f"Playback Count: {self.playback_count}")
        else:
            self.reserved_2: bytes = f.read(2)
            self.logger.debug(f"Reserved 2: {hex_log_str(self.reserved_2)}")

        self.u0_mask_table: U0MaskTable = U0MaskTable(f)

        self.flags: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Flags: {bin(self.flags)}")

        self.random_access_flag: bool = get_flag(self.flags, 0)
        self.logger.debug(f"Random Access Flag: {self.random_access_flag}")

        self.audio_mix_flag: bool = get_flag(self.flags, 1)
        self.logger.debug(f"Audio Mix Flag: {self.audio_mix_flag}")

        self.lossless_bypass_flag: bool = get_flag(self.flags, 2)
        self.logger.debug(f"Lossless Bypass Flag: {self.lossless_bypass_flag}")

        self.mvc_base_view_r_flag: bool = get_flag(self.flags, 3)
        self.logger.debug(f"MVC Base View R Flag: {self.mvc_base_view_r_flag}")

        self.sdr_conversion_notification_flag: bool = get_flag(self.flags, 4)
        self.logger.debug(f"SDR Conversion Notification Flag: {self.sdr_conversion_notification_flag}")
