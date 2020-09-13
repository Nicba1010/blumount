from typing import IO

from .logging_class import LoggingClass


class FormatClass(LoggingClass):

    def __init__(self, file_handle: IO):
        """
        Init
        """
        super().__init__()

        self.file_handle: IO = file_handle

    def seek(self, offset: int):
        self.logger.debug(f"Seeking from {self.file_handle.tell()} to {offset}")
        self.file_handle.seek(offset)
