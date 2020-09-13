from base import FileFormatWithMagic
from .clip_info import ClipInfo
from .clip_mark import ClipMark
from .cpi import CPI
from .header import ClpiHeader
from .program_info import ProgramInfo
from .sequence_info import SequenceInfo
from ..extensiondata import ExtensionData


class Clpi(FileFormatWithMagic[ClpiHeader]):

    def __init__(self, path: str):
        super().__init__(path, ClpiHeader)

        self.clip_info: ClipInfo = ClipInfo(self.file_handle)

        self.logger.debug(f"Seeking to sequence_info_start_address")
        self.seek(self.header.sequence_info_start_address)

        self.sequence_info: SequenceInfo = SequenceInfo(self.file_handle)

        self.logger.debug(f"Seeking to program_info_start_address")
        self.seek(self.header.program_info_start_address)

        self.program_info: ProgramInfo = ProgramInfo(self.file_handle)

        self.logger.debug(f"Seeking to cpi_start_address")
        self.seek(self.header.cpi_start_address)

        self.cpi: CPI = CPI(self.file_handle)

        self.logger.debug(f"Seeking to clip_mark_start_address")
        self.seek(self.header.clip_mark_start_address)

        self.clip_mark: ClipMark = ClipMark(self.file_handle)

        if self.header.extension_data_start_address != 0:
            self.extension_data: ExtensionData = ExtensionData(self.file_handle)
