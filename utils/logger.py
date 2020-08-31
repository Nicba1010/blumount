from logging import getLoggerClass, NOTSET, addLevelName


class Logger(getLoggerClass()):
    def __init__(self, name, level=NOTSET):
        super().__init__(name, level)
