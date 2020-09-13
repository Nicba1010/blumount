from typing import IO, List

from base import LoggingClass
from utils.utils import read_u32, Endianess, read_u16, hex_log_str, read_u8
from .angle import MultiAngleEntries
from .stn import StnTable
from .u0_mask_table import U0MaskTable


class PlayItem(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.length: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Length: {self.length}")

        self.clip_information_file_name: str = f.read(5).decode("ASCII")
        self.logger.debug(f"Clip Information File Name: {self.clip_information_file_name}")

        self.clip_codec_identifier: str = f.read(4).decode("ASCII")
        self.logger.debug(f"Clip Codec Identifier: {self.clip_codec_identifier}")

        self.flags_1: bytes = f.read(2)
        self.logger.debug(f"Flags 1: {hex_log_str(self.flags_1)}")

        self.is_multi_angle: bool = ((self.flags_1[1] & 0b00010000) >> 4) == 1
        self.logger.debug(f"Is Multi Angle: {self.is_multi_angle}")

        self.connection_condition: int = self.flags_1[1] & 0b00001111
        self.logger.debug(f"Connection Condition: {self.connection_condition}")

        self.ref_to_stc_id: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Reference to STC ID: {self.ref_to_stc_id}")

        self.in_time: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"In Time: {self.in_time}")

        self.out_time: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Out Time: {self.out_time}")

        self.u0_mask_table: U0MaskTable = U0MaskTable(f)

        self.flags_2: bytes = f.read(1)
        self.logger.debug(f"Flags 2: {hex_log_str(self.flags_2)}")

        self.random_access_flag: bool = ((self.flags_2[0] & 0b10000000) >> 7) == 1
        self.logger.debug(f"Random Access Flag: {self.random_access_flag}")

        self.still_mode: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Still Mode: {self.still_mode}")

        if self.still_mode == 0x01:
            self.still_time: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
            self.logger.debug(f"Still Time: {self.still_time}")
        else:
            self.reserved: bytes = f.read(2)
            self.logger.debug(f"Reserved: {hex_log_str(self.reserved)}")

        if self.is_multi_angle:
            self.multi_angle_entries: MultiAngleEntries = MultiAngleEntries(f)

        self.stn_table: StnTable = StnTable(f)

    @property
    def clip_information_file_names(self) -> List[str]:
        return [self.clip_information_file_name] + [
            x.clip_information_file_name
            for x
            in self.multi_angle_entries.angles
        ]

    @property
    def clip_codec_identifiers(self) -> List[str]:
        return [self.clip_codec_identifier] + [
            x.clip_codec_identifier
            for x
            in self.multi_angle_entries.angles
        ]

    @property
    def ref_to_stc_ids(self) -> List[int]:
        return [self.ref_to_stc_id] + [
            x.ref_to_stc_id
            for x
            in self.multi_angle_entries.angles
        ]
