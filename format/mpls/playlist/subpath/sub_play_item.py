from typing import IO, List

from base import LoggingClass
from format.mpls.playlist.subpath.clip.multi_clip_entries import MultiClipEntries
from utils.utils import read_u32, Endianess, hex_log_str, read_u8, read_u16


class SubPlayItem(LoggingClass):

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
        self.logger.debug(f"Clip Codec Identifier: {self.clip_information_file_name}")

        self.flags_1: bytes = f.read(2)
        self.logger.debug(f"Flags 1: {hex_log_str(self.flags_1)}")

        self.connection_condition: int = (self.flags_1[1] & 0b00011110) >> 1
        self.logger.debug(f"Connection Condition: {self.connection_condition}")

        self.is_multi_clip_entries: bool = (self.flags_1[1] & 0b00000001) == 1
        self.logger.debug(f"Is Multi Clip Entries: {self.is_multi_clip_entries}")

        self.ref_to_stc_id: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Reference to STC ID: {self.ref_to_stc_id}")

        self.in_time: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"In Time: {self.in_time}")

        self.out_time: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Out Time: {self.out_time}")

        self.sync_play_item_id: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Sync Play Item ID: {self.sync_play_item_id}")

        self.sync_start_pts_of_play_item: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Sync Start PTS of Play Item: {self.sync_start_pts_of_play_item}")

        if self.is_multi_clip_entries:
            self.multi_clip_entries: MultiClipEntries = MultiClipEntries(f)

    @property
    def clip_information_file_names(self) -> List[str]:
        return [self.clip_information_file_name] + [
            x.clip_information_file_name
            for x
            in self.multi_clip_entries.clips
        ]

    @property
    def clip_codec_identifiers(self) -> List[str]:
        return [self.clip_codec_identifier] + [
            x.clip_codec_identifier
            for x
            in self.multi_clip_entries.clips
        ]

    @property
    def ref_to_stc_ids(self) -> List[int]:
        return [self.ref_to_stc_id] + [
            x.ref_to_stc_id
            for x
            in self.multi_clip_entries.clips
        ]
