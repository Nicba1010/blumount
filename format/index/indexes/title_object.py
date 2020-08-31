from binascii import hexlify

from typing.io import IO

from utils.utils import read_u16, Endianess
from .access_type import AccessType
from .bdj_title_playback_type import BDJTitlePlaybackType
from .hdmv_title_playback_type import HDMVTitlePlaybackType
from .object import IndexObject
from .object_type import ObjectType


class TitleObject(IndexObject):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__(f)

        self.access_type: AccessType = AccessType((self.flags[0] & 0b00110000) >> 4)
        self.logger.debug(f"Access Type: {self.access_type}")

        if self.object_type == ObjectType.HDMV:
            self.object_flags: bytes = f.read(2)
            self.logger.debug(f"Object Flags: {hexlify(self.flags)}")

            self.hdmv_title_playback_type: HDMVTitlePlaybackType = HDMVTitlePlaybackType(
                (self.object_flags[0] & 0b11000000) >> 6
            )
            self.logger.debug(f"HDMV Title Playback Type: {self.hdmv_title_playback_type}")

            self.mobj_id_ref: int = read_u16(f, endianess=Endianess.BIG_ENDIAN)
            """
            Represents the ID of a movie indexes used in the top menu
            """
            self.logger.debug(f"Movie Object Id Reference: {self.mobj_id_ref}")

            self.reserved: bytes = f.read(4)
            self.logger.debug(f"Reserved: {hexlify(self.reserved)}")
        elif self.object_type == ObjectType.BDJ:
            self.object_flags: bytes = f.read(2)
            self.logger.debug(f"Object Flags: {hexlify(self.flags)}")

            self.bdj_title_playback_type: BDJTitlePlaybackType = BDJTitlePlaybackType(
                (self.object_flags[0] & 0b11000000) >> 6
            )
            self.logger.debug(f"BD-J Object Playback Type: {self.bdj_title_playback_type}")

            self.bdjo_file_name: int = f.read(5).decode("ASCII")
            """
            Represents the file name of a BD-J indexes used in the top menu
            """
            self.logger.debug(f"BD-J Object File Name: {self.bdjo_file_name}")

            self.reserved: bytes = f.read(1)
            self.logger.debug(f"Reserved: {hexlify(self.reserved)}")
