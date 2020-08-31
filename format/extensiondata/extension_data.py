from typing import List

from typing.io import IO

from base import LoggingClass
from utils.utils import Endianess, read_u32, read_u8, hex_log_str
from .entry import Entry


class ExtensionData(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.length: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Length: {self.length}")

        if self.length != 0:
            self.data_block_start_address: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
            self.logger.debug(f"Data Block Start Address: {self.data_block_start_address}")

            self.reserved_for_word_align: int = f.read(3)
            self.logger.debug(f"Reserved For Word Align: {self.reserved_for_word_align}")

            self.number_of_ext_data_entries: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
            self.logger.debug(f"Number of Ext Data Entries: {self.number_of_ext_data_entries}")

            self.entries: List[Entry] = list()
            for entry_index in range(self.number_of_ext_data_entries):
                self.logger.debug(f"Reading Entry {entry_index}")
                self.entries.append(Entry(f))

            self.data_block: bytes = f.read(4 + self.length - self.data_block_start_address)
            self.logger.debug(f"Data Block: {hex_log_str(self.data_block)}")
