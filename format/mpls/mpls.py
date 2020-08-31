from base import FileFormatWithMagic
from .header import MplsHeader
from .playlist import PlayList
from .playlist.app_info_play_list import AppInfoPlayList
from ..extensiondata import ExtensionData


class Mpls(FileFormatWithMagic[MplsHeader]):

    def __init__(self, path: str):
        super().__init__(path, MplsHeader)

        self.app_info_play_list: AppInfoPlayList = AppInfoPlayList(self.file_handle)

        self.logger.debug(
            f"Seeking from {self.file_handle.tell()} to "
            f"playlist_start_address at {self.header.playlist_start_address}"
        )
        self.file_handle.seek(self.header.playlist_start_address)

        self.play_list: PlayList = PlayList(self.file_handle)

        # TODO: MARK

        # self.logger.debug(
        #     f"Seeking from {self.file_handle.tell()} to "
        #     f"extension_data_start_address at {self.header.extension_data_start_address}"
        # )
        # self.file_handle.seek(self.header.extension_data_start_address)
        #
        # self.extension_data: ExtensionData = ExtensionData(self.file_handle)
