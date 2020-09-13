from typing import IO, List

from base import LoggingClass
from utils.utils import Endianess, read_u8, read_u32, read_u16
from .stream_in_ps import StreamInPS


class Program(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.spn_program_sequence_start: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"SPN Program Sequence Start: {self.spn_program_sequence_start}")

        self.program_map_pid: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Program Map PID: {self.program_map_pid}")

        self.number_of_streams_in_ps: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of Streams in PS: {self.number_of_streams_in_ps}")

        self.number_of_groups_in_ps: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of Groups in PS: {self.number_of_groups_in_ps}")

        self.streams: List[StreamInPS] = list()
        for stream_in_ps_index in range(self.number_of_streams_in_ps):
            self.logger.debug(f"Reading Stream in PS {stream_in_ps_index}")
            self.streams.append(StreamInPS(f))
