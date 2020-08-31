from typing import IO, List

from base import LoggingClass
from utils.utils import read_u32, Endianess, read_u16, hex_log_str, read_u8


class Angle(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.clip_information_file_name: str = f.read(5).decode("ASCII")
        self.logger.debug(f"Clip Information File Name: {self.clip_information_file_name}")

        self.clip_codec_identifier: str = f.read(4).decode("ASCII")
        self.logger.debug(f"Clip Codec Identifier: {self.clip_information_file_name}")

        self.ref_to_stc_id: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Reference to STC ID: {self.ref_to_stc_id}")