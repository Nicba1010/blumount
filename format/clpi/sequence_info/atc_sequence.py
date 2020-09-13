from typing import IO, List

from base import LoggingClass
from utils.utils import Endianess, read_u8, read_u32
from .stc_sequence import StcSequence


class AtcSequence(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.spn_atc_start: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"SPN ATC Start: {self.spn_atc_start}")

        self.number_of_stc_sequences: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of STC Sequences: {self.number_of_stc_sequences}")

        self.offset_stc_id: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Offset STC ID: {self.offset_stc_id}")

        self.stc_sequences: List[StcSequence] = list()
        for stc_sequence_index in range(self.number_of_stc_sequences):
            self.logger.debug(f"Reading STC Sequence {stc_sequence_index}")
            self.stc_sequences.append(StcSequence(f))
