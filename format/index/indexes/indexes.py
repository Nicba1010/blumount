from typing import IO, List

from base import LoggingClass
from utils.utils import read_u32, Endianess, read_u16
from .first_playback_object import FirstPlaybackObject
from .title_object import TitleObject
from .top_menu_object import TopMenuObject


class Indexes(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.length: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Length: {self.length}")

        self.first_playback_object: FirstPlaybackObject = FirstPlaybackObject(f)

        self.top_menu_object: TopMenuObject = TopMenuObject(f)

        self.number_of_titles: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of Titles: {self.number_of_titles}")

        self.titles: List[TitleObject] = list()
        for title_index in range(self.number_of_titles):
            self.logger.debug(f"Reading Title Object {title_index}")
            self.titles.append(TitleObject(f))
