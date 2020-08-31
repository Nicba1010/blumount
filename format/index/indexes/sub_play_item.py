from typing import IO, List

from base import LoggingClass
from utils.utils import read_u32, Endianess, hex_log_str, read_u8
from ...index.indexes.sub_path_type import SubPathType


class SubPlayItem(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.length: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Length: {self.length}")

        self.reserved_1: bytes = f.read(1)
        self.logger.debug(f"Reserved 1: {hex_log_str(self.reserved_1)}")

        self.sub_path_type: SubPathType = SubPathType(read_u8(f, endianess=Endianess.BIG_ENDIAN))
        self.logger.debug(f"Sub Path Type: {self.sub_path_type}")

        self.flags_1: bytes = f.read(2)
        self.logger.debug(f"Flags 1: {hex_log_str(self.flags_1)}")

        self.is_repeat_sub_path: bool = (self.flags_1[1] & 0b00000001) == 1
        self.logger.debug(f"Is Repeat Sub Path: {self.is_repeat_sub_path}")

        self.reserved_2: bytes = f.read(1)
        self.logger.debug(f"Reserved 2: {hex_log_str(self.reserved_2)}")

        self.num_sub_play_items: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Num Sub Play Items: {self.length}")

        self.sub_play_items: List[SubPlayItem] = []
        for index in range(self.num_video):
            self.logger.debug(f"Reading Video Stream {index}")
            self.video_streams.append(Stream(f))
