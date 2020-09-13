from typing import IO, List

from base import LoggingClass
from utils.utils import Endianess, read_u8
from format.mpls.playlist.subpath.clip.clip import Clip


class MultiClipEntries(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.number_of_clips: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of Clips: {self.number_of_clips}")

        self.reserved: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Reserved: {self.reserved}")

        self.clips: List[Clip] = []
        for index in range(self.number_of_clips):
            self.logger.debug(f"Reading Clip {index}")
            self.clips.append(Clip(f))
