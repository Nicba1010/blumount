from binascii import hexlify
from typing import IO

from base.header import MagicFileHeader
from utils.utils import read_u32, Endianess
from format.version import BluRayVersion


class IndexHeader(MagicFileHeader):
    def __init__(self, f: IO):
        super().__init__(f)

        self.version: BluRayVersion = BluRayVersion(f.read(4).decode("ASCII"))
        self.logger.debug(f'Version: {self.version.value}')

        self.indexes_start_address: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f'Index Start: {self.indexes_start_address}')

        self.extension_data_start_address: int = read_u32(f, endianess=Endianess.BIG_ENDIAN)
        self.logger.debug(f'Extension Data Start: {self.extension_data_start_address}')

        self.reserved: bytes = f.read(192 // 8)
        self.logger.debug(f'Reserved: {hexlify(self.reserved)}')

    @property
    def magic(self) -> bytes:
        return b'INDX'
