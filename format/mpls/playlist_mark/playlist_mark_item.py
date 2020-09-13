from typing import IO

from base import LoggingClass
from utils.utils import read_u32, Endianess, read_u16, read_u8
from .mark_type import MarkType


class PlaylistMarkItem(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.reserved: int = f.read(1)
        self.logger.debug(f"Reserved: {self.reserved}")

        self.mark_type: MarkType = MarkType(read_u8(f, endianess=Endianess.BIG_ENDIAN))
        self.logger.debug(f"Mark Type: {self.mark_type}")

        self.ref_to_play_item_id: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Ref To Play Item ID: {self.ref_to_play_item_id}")

        self.mark_timestamp: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Mark Timestamp: {self.mark_timestamp}")

        self.entry_esp_id: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Entry ESP Id: {self.entry_esp_id}")

        self.duration: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Duration: {self.duration}")
