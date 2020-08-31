from typing import IO, List

from base import LoggingClass
from utils.utils import Endianess, read_u8
from .angle import Angle


class MultiClipEntries(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.number_of_angles: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of Angles: {self.number_of_angles}")

        self.flags: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Flags: {self.flags}")

        self.is_different_audios: bool = ((self.flags & 0b00000010) >> 1) == 1
        self.logger.debug(f"Is Different Audios: {self.is_different_audios}")

        self.is_seamless_angle_change: bool = ((self.flags & 0b00000001) >> 1) == 1
        self.logger.debug(f"Is Seamless Angle Change: {self.is_seamless_angle_change}")

        self.angles: List[Angle] = []
        for index in range(self.number_of_angles):
            self.logger.debug(f"Reading Angle {index}")
            self.angles.append(Angle(f))
