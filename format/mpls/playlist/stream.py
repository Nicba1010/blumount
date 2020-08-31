from typing import IO

from base import LoggingClass
from utils.utils import Endianess, read_u16, read_u8, read_u32
from .audio_format import AudioFormat
from .character_code import CharacterCode
from .coding_type import CodingType
from .color_space import ColorSpace
from .dynamic_range_type import DynamicRangeType
from .frame_rate import FrameRate
from .sample_rate import SampleRate
from .stream_type import StreamType
from .video_format import VideoFormat


class Stream(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.length: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Length: {self.length}")

        current_position: int = f.tell()
        self.logger.debug(f"Current Position: {current_position}")

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

        self.logger.debug(
            f"Seeking from {f.tell()} to "
            f"current_position + length at {current_position + self.length}"
        )
        f.seek(current_position + self.length)

        self.attributes_length: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f"Attributes Length: {self.attributes_length}")

        current_position: int = f.tell()
        self.logger.debug(f"Current Position: {current_position}")

        self.coding_type: CodingType = CodingType(read_u8(f, endianess=Endianess.BIG_ENDIAN))
        self.logger.debug(f"Coding Type: {self.coding_type}")

        if self.coding_type in [
            CodingType.MPEG1_VIDEO_PRIMARY_SECONDARY,
            CodingType.MPEG2_VIDEO_PRIMARY_SECONDARY,
            CodingType.MPEG4_AVC_VIDEO_PRIMARY_SECONDARY,
            CodingType.MPEG4_MVC_VIDEO_PRIMARY_SECONDARY,
            CodingType.VC1_VIDEO_PRIMARY_SECONDARY
        ]:
            self.data: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
            self.logger.debug(f"Data: {self.data}")

            self.format: VideoFormat = VideoFormat((self.data & 0b11110000) >> 4)
            self.logger.debug(f"Video Format: {self.format}")

            self.rate: FrameRate = FrameRate(self.data & 0b00001111)
            self.logger.debug(f"Frame Rate: {self.rate}")
        elif self.coding_type in [
            CodingType.HEVC_VIDEO_PRIMARY_SECONDARY
        ]:
            self.data: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
            self.logger.debug(f"Data: {self.data}")

            self.format: VideoFormat = VideoFormat((self.data & 0b1111000000000000) >> 12)
            self.logger.debug(f"Video Format: {self.format}")

            self.rate: FrameRate = FrameRate((self.data & 0b0000111100000000) >> 8)
            self.logger.debug(f"Frame Rate: {self.rate}")

            self.dynamic_range_type: DynamicRangeType = DynamicRangeType((self.data & 0b11110000) >> 8)
            self.logger.debug(f"Dynamic Range Type: {self.dynamic_range_type}")

            self.color_space: ColorSpace = ColorSpace((self.data & 0b00001111))
            self.logger.debug(f"Frame Rate: {self.color_space}")
        elif self.coding_type in [
            CodingType.MPEG1_AUDIO_PRIMARY_SECONDARY,
            CodingType.MPEG2_AUDIO_PRIMARY_SECONDARY,
            CodingType.LPCM_AUDIO_PRIMARY,
            CodingType.DOLBY_DIGITAL_AUDIO_PRIMARY,
            CodingType.DTS_AUDIO_PRIMARY,
            CodingType.DOLBY_DIGITAL_TRUEHD_AUDIO_PRIMARY,
            CodingType.DOLBY_DIGITAL_PLUS_AUDIO_PRIMARY,
            CodingType.DTS_HD_HIGH_RESOLUTION_AUDIO_PRIMARY,
            CodingType.DTS_HD_MASTER_AUDIO_AUDIO_PRIMARY,
            CodingType.DOLBY_DIGITAL_PLUS_AUDIO_SECONDARY,
            CodingType.DTS_HD_AUDIO_SECONDARY
        ]:
            self.data: int = read_u8(f, endianess=Endianess.BIG_ENDIAN)
            self.logger.debug(f"Data: {bin(self.data)}")

            self.format: AudioFormat = AudioFormat((self.data & 0b11110000) >> 4)
            self.logger.debug(f"Audio Format: {self.format}")

            self.rate: SampleRate = SampleRate(self.data & 0b00001111)
            self.logger.debug(f"Sample Rate: {self.rate}")

            self.language: str = f.read(3).decode("ASCII")
            self.logger.debug(f"Language Code: {self.language}")
        elif self.coding_type in [
            CodingType.PRESENTATION_GRAPHICS_SUBTITLES,
            CodingType.INTERACTIVE_GRAPHICS_MENU
        ]:
            self.language: str = f.read(3).decode("ASCII")
            self.logger.debug(f"Language Code: {self.language}")
        elif self.coding_type in [
            CodingType.TEXT_SUBTITLES
        ]:
            self.char_code: CharacterCode = CharacterCode(read_u8(f, endianess=Endianess.BIG_ENDIAN))
            self.logger.debug(f"Character Code: {self.char_code}")

            self.language: str = f.read(3).decode("ASCII")
            self.logger.debug(f"Language Code: {self.language}")


        self.logger.debug(
            f"Seeking from {f.tell()} to "
            f"current_position + attributes_length at {current_position + self.attributes_length}"
        )
        f.seek(current_position + self.attributes_length)
