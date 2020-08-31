from typing import IO

from base import LoggingClass
from utils.utils import Endianess, read_u16, read_u8
from .coding_type import CodingType
from .stream_type import StreamType


class Stream(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.length: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Length: {self.length}")

        self.stream_type: StreamType = StreamType(read_u8(f, endianess=Endianess.BIG_ENDIAN))
        self.logger.debug(f"Stream Type: {self.stream_type}")

        if self.stream_type == StreamType.USED_BY_PLAY_ITEM:
            self.pid: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
            self.logger.debug(f"PID: {self.pid}")
        elif self.stream_type == StreamType.USED_BY_SUB_PATH_TYPE_23456:
            self.sub_path_id: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
            self.logger.debug(f"Sub Path ID: {self.sub_path_id}")

            self.sub_clip_id: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
            self.logger.debug(f"Sub Clip ID: {self.sub_clip_id}")

            self.pid: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
            self.logger.debug(f"PID: {self.pid}")
        elif self.stream_type == StreamType.USED_BY_SUB_PATH_TYPE_7:
            self.sub_path_id: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
            self.logger.debug(f"Sub Path ID: {self.sub_path_id}")

            self.pid: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
            self.logger.debug(f"PID: {self.pid}")

        # TODO MAYBE m_bc->set_bit_position((length + position) * 8)

        self.coding_type: CodingType = CodingType(read_u8(f, endianess=Endianess.BIG_ENDIAN))
        self.logger.debug(f"Coding Type: {self.coding_type}")

        if self.coding_type in [CodingType.MPEG2_VIDEO_PRIMARY_SECONDARY, CodingType.MPEG4_AVC_VIDEO_PRIMARY_SECONDARY,
                                CodingType.VC1_VIDEO_PRIMARY_SECONDARY]:
            self.format_and_rate: int = f.read(1)
            self.logger.debug(f"Format and Rate: {self.format_and_rate}")

            self.format: int = (self.format_and_rate & 0x11110000) >> 4
            self.logger.debug(f"Format: {self.format}")

            self.rate: int = self.format_and_rate & 0x00001111
            self.logger.debug(f"Rate: {self.rate}")
        elif self.coding_type in [CodingType.LPCM_AUDIO_PRIMARY, CodingType.AC3_AUDIO_PRIMARY,
                                  CodingType.DTS_AUDIO_PRIMARY, CodingType.EAC3_AUDIO_PRIMARY,
                                  CodingType.DTS_HD_AUDIO_PRIMARY, CodingType.DTS_HD_XLL_AUDIO_PRIMARY,
                                  CodingType.EAC3_AUDIO_SECONDARY, CodingType.DTS_HD_AUDIO_SECONDARY]:
            self.format_and_rate: int = f.read(1)
            self.logger.debug(f"Format and Rate: {self.format_and_rate}")

            self.format: int = (self.format_and_rate & 0x11110000) >> 4
            self.logger.debug(f"Format: {self.format}")

            self.rate: int = self.format_and_rate & 0x00001111
            self.logger.debug(f"Rate: {self.rate}")

            self.language: str = f.read(3).decode("ASCII")
            self.logger.debug(f"Language: {self.language}")
        elif self.coding_type in [CodingType.PRESENTATION_GRAPHICS_SUBTITLES, CodingType.INTERACTIVE_GRAPHICS_MENU]:
            self.language: str = f.read(3).decode("ASCII")
            self.logger.debug(f"Language: {self.language}")
        elif self.coding_type in [CodingType.TEXT_SUBTITLES]:
            self.char_code: str = f.read(1).decode("ASCII")
            self.logger.debug(f"Char Code: {self.char_code}")

            self.language: str = f.read(3).decode("ASCII")
            self.logger.debug(f"Language: {self.language}")
