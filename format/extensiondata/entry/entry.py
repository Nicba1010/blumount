from typing.io import IO

from base import LoggingClass
from utils.utils import Endianess, read_u32, read_u16


class Entry(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.id1: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"ID1: {self.id1}")

        self.id2: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"ID2: {self.id2}")

        self.ext_data_start_address: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Ext Data Start Address: {self.ext_data_start_address}")

        self.ext_data_length: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Ext Data Length: {self.ext_data_length}")
