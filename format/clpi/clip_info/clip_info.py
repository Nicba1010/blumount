from typing import IO

from base import LoggingClass
from base.utils import get_flag
from utils.utils import Endianess, read_u8, hex_log_str, read_u32
from .application_type import ApplicationType
from .clip_stream_type import ClipStreamType
from .following_clip_stream_type import FollowingClipStreamType
from .ts_type_info_block import TsTypeInfoBlock


class ClipInfo(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.length: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Length: {self.length}")

        self.reserved_1: bytes = f.read(16 // 8)
        self.logger.debug(f"Reserved 1: {hex_log_str(self.reserved_1)}")

        self.clip_stream_type: ClipStreamType = ClipStreamType(read_u8(f, endianess=Endianess.BIG_ENDIAN))
        self.logger.debug(f"Clip Stream Type: {self.clip_stream_type}")

        self.application_type: ApplicationType = ApplicationType(read_u8(f, endianess=Endianess.BIG_ENDIAN))
        self.logger.debug(f"Application Type: {self.application_type}")

        self.flags: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Flags: {bin(self.flags)}")

        self.is_cc5: bool = get_flag(self.flags, 31)
        self.logger.debug(f"Is CC5 / Is ATC Delta: {self.is_cc5}")

        self.ts_recording_rate: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"TS Recording Rate: {self.ts_recording_rate}")

        self.number_of_source_packets: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Number of Source Packets: {self.number_of_source_packets}")

        self.reserved_2: bytes = f.read(1024 // 8)
        self.logger.debug(f"Reserved 2: {hex_log_str(self.reserved_2)}")

        self.ts_type_info_block: TsTypeInfoBlock = TsTypeInfoBlock(f)

        if self.is_cc5:
            self.reserved_3: bytes = f.read(8 // 8)
            self.logger.debug(f"Reserved 3: {hex_log_str(self.reserved_3)}")

            self.following_clip_stream_type: FollowingClipStreamType = FollowingClipStreamType(
                read_u8(f, endianess=Endianess.BIG_ENDIAN)
            )
            self.logger.debug(f"Following Clip Stream Type: {self.following_clip_stream_type}")

            self.reserved_4: bytes = f.read(32 // 8)
            self.logger.debug(f"Reserved 4: {hex_log_str(self.reserved_4)}")

            self.following_clip_information_file_name: str = f.read(5).decode("ASCII")
            self.logger.debug(f"Following Clip Information File Name: {self.following_clip_information_file_name}")

            self.following_clip_codec_identifier: str = f.read(4).decode("ASCII")
            self.logger.debug(f"Following Clip Codec Identifier: {self.following_clip_information_file_name}")

            self.reserved_5: bytes = f.read(8 // 8)
            self.logger.debug(f"Reserved 5: {hex_log_str(self.reserved_5)}")
