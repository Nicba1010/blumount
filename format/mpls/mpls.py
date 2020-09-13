from base import FileFormatWithMagic
from .app_info_playlist import AppInfoPlaylist
from .header import MplsHeader
from .playlist import Playlist
from .playlist_mark import PlaylistMark
from ..extensiondata import ExtensionData


class Mpls(FileFormatWithMagic[MplsHeader]):

    def __init__(self, path: str):
        super().__init__(path, MplsHeader)

        self.app_info_play_list: AppInfoPlaylist = AppInfoPlaylist(self.file_handle)

        self.logger.debug(f"Seeking to playlist_start_address")
        self.seek(self.header.playlist_start_address)

        self.playlist: Playlist = Playlist(self.file_handle)

        self.playlist_mark: PlaylistMark = PlaylistMark(self.file_handle)

        self.logger.debug(f"Seeking to extension_data_start_address")
        self.seek(self.header.extension_data_start_address)

        self.extension_data: ExtensionData = ExtensionData(self.file_handle)
