from base import FileFormatWithMagic
from utils.utils import hex_log_str
from .header import IndexHeader
from .indexes import Indexes
from ..extensiondata import ExtensionData


class Index(FileFormatWithMagic[IndexHeader]):

    def __init__(self, path: str):
        super().__init__(path, IndexHeader)

        self.app_info_bdmv: bytes = self.file_handle.read(
            self.header.indexes_start_address - self.file_handle.tell()
        )
        self.logger.debug(f"App Info BDMV: {hex_log_str(self.app_info_bdmv)}")

        self.logger.debug(
            f"Seeking from {self.file_handle.tell()} to "
            f"indexes_start_address at {self.header.indexes_start_address}"
        )
        self.file_handle.seek(self.header.indexes_start_address)

        self.indexes: Indexes = Indexes(self.file_handle)

        self.logger.debug(
            f"Seeking from {self.file_handle.tell()} to "
            f"extension_data_start_address at {self.header.extension_data_start_address}"
        )
        self.file_handle.seek(self.header.extension_data_start_address)

        self.extension_data: ExtensionData = ExtensionData(self.file_handle)
