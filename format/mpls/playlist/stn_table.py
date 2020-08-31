from typing import IO, List

from base import LoggingClass
from utils.utils import Endianess, read_u8, read_u16, hex_log_str
from .stream import Stream


class StnTable(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.length: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Length: {self.length}")

        self.reserved_1: bytes = f.read(2)
        self.logger.debug(f"Reserved 1: {hex_log_str(self.reserved_1)}")

        self.num_video: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of Video Streams: {self.num_video}")

        self.num_audio: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of Audio Streams: {self.num_audio}")

        self.num_pg: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of PG Streams: {self.num_pg}")

        self.num_ig: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of IG Streams: {self.num_ig}")

        self.num_secondary_audio: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of Secondary Audio Streams: {self.num_secondary_audio}")

        self.num_secondary_video: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of Secondary Video Streams: {self.num_secondary_video}")

        self.num_pip_pg: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of PIP PG Streams: {self.num_pip_pg}")

        self.reserved_2: bytes = f.read(5)
        self.logger.debug(f"Reserved 2: {hex_log_str(self.reserved_2)}")

        self.video_streams: List[Stream] = []
        for index in range(self.num_video):
            self.logger.debug(f"Reading Video Stream {index}")
            self.video_streams.append(Stream(f))

        self.audio_streams: List[Stream] = []
        for index in range(self.num_audio):
            self.logger.debug(f"Reading Audio Stream {index}")
            self.audio_streams.append(Stream(f))

        self.pg_streams: List[Stream] = []
        for index in range(self.num_pg):
            self.logger.debug(f"Reading PG Stream {index}")
            self.pg_streams.append(Stream(f))
