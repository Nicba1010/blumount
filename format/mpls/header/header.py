from binascii import hexlify
from typing import IO

from base.header import MagicFileHeader
from utils.utils import read_u32, Endianess
from format.version import BluRayVersion


class MplsHeader(MagicFileHeader):
    def __init__(self, f: IO):
        super().__init__(f)

        self.version: BluRayVersion = BluRayVersion(f.read(4).decode("ASCII"))
        self.logger.debug(f'Version: {self.version.value}')

        self.playlist_start_address: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f'Playlist Start Address: {self.playlist_start_address}')

        self.playlist_mark_start_address: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f'Playlist Mark Start Address: {self.playlist_start_address}')

        self.extension_data_start_address: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f'Extension Data Start: {self.extension_data_start_address}')

        self.reserved: bytes = f.read(160 // 8)
        self.logger.debug(f'Reserved: {hexlify(self.reserved)}')

    @property
    def magic(self) -> bytes:
        return b'MPLS'
