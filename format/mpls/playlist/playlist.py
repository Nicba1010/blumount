from typing import IO, List

from base import LoggingClass
from utils.utils import read_u32, Endianess, read_u16, hex_log_str
from .play_item import PlayItem


class PlayList(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.length: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Length: {self.length}")

        self.reserved: bytes = f.read(2)
        self.logger.debug(f"Reserved: {hex_log_str(self.reserved)}")

        self.number_of_play_items: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of Play Items: {self.number_of_play_items}")

        self.number_of_sub_paths: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of Sub Paths: {self.number_of_sub_paths}")

        self.play_items: List[PlayItem] = list()
        for index in range(self.number_of_play_items):
            self.logger.debug(f"Reading Play Item {index}")
            self.play_items.append(PlayItem(f))

        self.sub_paths: List[SubPath] = list()
        for index in range(self.number_of_play_items):
            self.logger.debug(f"Reading Sub Path {index}")
            self.sub_paths.append(SubPath(f))
