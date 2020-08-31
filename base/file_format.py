import os
from typing import IO, TypeVar, Generic, Type

from .errors import EmptyFileException, InvalidFileHashException
from .header import MagicFileHeader
from .logging_class import LoggingClass


class FileFormat(LoggingClass):

    def __init__(self, path: str):
        super().__init__()

        #: File Path
        self.path: str = path
        self.logger.debug(f'Parsing file: {self.path}')

        if os.stat(self.path).st_size == 0:
            raise EmptyFileException()

        #: File Handle
        self.file_handle: IO = self.get_file_handle()

    def get_file_handle(self) -> IO:
        return open(self.path, 'rb')

    # noinspection PyMethodMayBeStatic
    def verify_hash(self) -> bool:
        return True

    def __del__(self):
        self.logger.debug(f'Cleaning up, read {self.file_handle.tell()}/{os.path.getsize(self.path)}...')
        if not self.file_handle.closed:
            self.file_handle.close()


T = TypeVar('T', bound=MagicFileHeader)


class FileFormatWithMagic(FileFormat, Generic[T]):

    def __init__(self, path: str, header_class: Type[T]):
        super().__init__(path)
        self.__header_class = header_class
        self.__header = self.__header_class(self.file_handle)

    @property
    def header(self) -> T:
        return self.__header
