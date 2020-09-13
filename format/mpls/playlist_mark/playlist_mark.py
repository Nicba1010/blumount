from typing import IO, List

from base import LoggingClass
from .playlist_mark_item import PlaylistMarkItem
from utils.utils import read_u32, Endianess, read_u16


class PlaylistMark(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.length: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Length: {self.length}")

        self.number_of_playlist_mark_items: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of Playlist Mark Items: {self.number_of_playlist_mark_items}")

        self.playlist_mark_items: List[PlaylistMarkItem] = list()
        for index in range(self.number_of_playlist_mark_items):
            self.logger.debug(f"Reading Playlist Mark Item {index}")
            self.playlist_mark_items.append(PlaylistMarkItem(f))

