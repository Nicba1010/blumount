from typing import IO, List

from base import LoggingClass
from utils.utils import Endianess, read_u8, hex_log_str, read_u32
from .atc_sequence import AtcSequence


class SequenceInfo(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.length: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Length: {self.length}")

        self.reserved_1: bytes = f.read(8 // 8)
        self.logger.debug(f"Reserved 1: {hex_log_str(self.reserved_1)}")

        self.number_of_atc_sequences: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of ATC Sequences: {self.number_of_atc_sequences}")

        self.atc_sequences: List[AtcSequence] = list()
        for atc_sequence_index in range(self.number_of_atc_sequences):
            self.logger.debug(f"Reading ATC Sequence {atc_sequence_index}")
            self.atc_sequences.append(AtcSequence(f))
