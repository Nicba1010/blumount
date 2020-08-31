from binascii import hexlify

from typing.io import IO

from base import LoggingClass
from .object_type import ObjectType


class IndexObject(LoggingClass):

    def __init__(self, f: IO):
        """
        Init
        """
        super().__init__()

        self.flags: bytes = f.read(4)
        self.logger.debug(f"Flags: {hexlify(self.flags)}")

        self.object_type: ObjectType = ObjectType((self.flags[0] & 0b11000000) >> 6)
        self.logger.debug(f"Object Type: {self.object_type}")
