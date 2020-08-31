from binascii import hexlify

from typing.io import IO

from utils.utils import read_u16, Endianess
from .object import IndexObject
from .object_type import ObjectType


class TopMenuObject(IndexObject):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__(f)

        if self.object_type == ObjectType.HDMV:
            self.object_flags: bytes = f.read(2)
            self.logger.debug(f"Object Flags: {hexlify(self.flags)}")

            assert (self.object_flags[0] & 0b11000000) >> 6 == 0b01

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

            assert (self.object_flags[0] & 0b11000000) >> 6 == 0b11

            self.bdjo_file_name: int = f.read(5).decode("ASCII")
            """
            Represents the file name of a BD-J indexes used in the top menu
            """
            self.logger.debug(f"BD-J Object File Name: {self.bdjo_file_name}")

            self.reserved: bytes = f.read(1)
            self.logger.debug(f"Reserved: {hexlify(self.reserved)}")
