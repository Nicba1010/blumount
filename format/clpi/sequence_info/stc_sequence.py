from typing import IO

from base import LoggingClass
from utils.utils import Endianess, read_u32, read_u16


class StcSequence(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.pcrp_id: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"PCRP Id: {self.pcrp_id}")

        self.spn_stc_start: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"SPN STC Start: {self.spn_stc_start}")

        self.presentation_start_time: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Presentation Start Time: {self.presentation_start_time}")

        self.presentation_end_time: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Presentation End Time: {self.presentation_end_time}")
