from typing import IO, List

from base import LoggingClass
from utils.utils import Endianess, read_u8, hex_log_str, read_u32
from .program import Program


class ProgramInfo(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.length: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Length: {self.length}")

        self.reserved_1: bytes = f.read(8 // 8)
        self.logger.debug(f"Reserved 1: {hex_log_str(self.reserved_1)}")

        self.number_of_programs: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of Programs: {self.number_of_programs}")

        self.programs: List[Program] = list()
        for program_index in range(self.number_of_programs):
            self.logger.debug(f"Program Index {program_index}")
            self.programs.append(Program(f))
