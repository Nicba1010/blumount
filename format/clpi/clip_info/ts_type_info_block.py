from typing import IO

from base import LoggingClass
from utils.utils import Endianess, read_u16, hex_log_str


class TsTypeInfoBlock(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.length: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Length: {self.length}")

        self.reserved: bytes = f.read((256 - 16) // 8)
        self.logger.debug(f"Reserved: {hex_log_str(self.reserved_1)}")
