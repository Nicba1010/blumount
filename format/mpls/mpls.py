from base import FileFormatWithMagic
from utils.utils import hex_log_str
from .header import MplsHeader
from ..extensiondata import ExtensionData
from .playlist import PlayList


class Mpls(FileFormatWithMagic[MplsHeader]):

    def __init__(self, path: str):
        super().__init__(path, MplsHeader)

        # App info playlist check

        self.app_info_play_list: bytes = self.file_handle.read(
            self.header.playlist_start_address - self.file_handle.tell()
        )
        self.logger.debug(f"App Info Playlist: {hex_log_str(self.app_info_play_list)}")

        self.logger.debug(
            f"Seeking from {self.file_handle.tell()} to "
            f"playlist_start_address at {self.header.playlist_start_address}"
        )
        self.file_handle.seek(self.header.playlist_start_address)

        self.play_list: PlayList = PlayList(self.file_handle)

        # self
        #
        # self.indexes_length: int = read_u32(self.file_handle, endianess=Endianess.BIG_ENDIAN)
        # self.logger.debug(f"Indexes Length: {self.indexes_length}")
        #
        # self.first_playback_object: FirstPlaybackObject = FirstPlaybackObject(self.file_handle)
        #
        # self.top_menu_object: TopMenuObject = TopMenuObject(self.file_handle)
        #
        # self.number_of_titles: int = read_u16(self.file_handle, endianess=Endianess.BIG_ENDIAN)
        # self.logger.debug(f"Number of Titles: {self.number_of_titles}")
        #
        # self.titles: List[TitleObject] = list()
        # for title_index in range(self.number_of_titles):
        #     self.logger.debug(f"Reading Title Object {title_index}")
        #     self.titles.append(TitleObject(self.file_handle))
        #
        #
        self.logger.debug(
            f"Seeking from {self.file_handle.tell()} to "
            f"extension_data_start_address at {self.header.extension_data_start_address}"
        )
        self.file_handle.seek(self.header.extension_data_start_address)

        self.extension_data: ExtensionData = ExtensionData(self.file_handle)

        # sha1 = hashlib.sha1()
        # self.file_handle.seek(0x00)
        # sha1.update(self.file_handle.read(0x80))
        #
        # # TODO: Why DEBUG pkg hash always fail?
        # if sha1.digest()[-8:] != self.header.header_sha1_hash and self.header.revision != PkgRevision.DEBUG:
        #     raise InvalidPKGHeaderHashException()
        # else:
        #     self.logger.info('Header SHA1 Hash Verified!')
        #
        # self.metadata: List[PkgMetadata] = []
        # self.file_handle.seek(self.header.metadata_offset)
        #
        # for metadata_index in range(0, self.header.metadata_count):
        #     self.logger.info(f'Processing metadata #{metadata_index}:')
        #     self.metadata.append(PkgMetadata.create(self.file_handle))
        #
        # self.file_handle.seek(self.header.data_offset)
        # self.files: List[PkgEntry] = []
        # with PkgInternalIO(self.file_handle, self.header, self.internal_fs_key) as f:
        #     for item_index in range(0, self.header.item_count):
        #         self.logger.info(f'Processing file #{item_index}:')
        #         self.file_handle.seek(self.header.data_offset + PkgEntry.size() * item_index)
        #         self.files.append(PkgEntry.read_from_file(f))
