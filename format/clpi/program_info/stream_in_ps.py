from typing import IO

from base import LoggingClass
from format.mpls.playlist.play_item.stn.stream import Stream
from utils.utils import Endianess, read_u16


class StreamInPS(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.stream_id: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Stream Id: {self.stream_id}")

        self.stream: Stream = Stream(f)
