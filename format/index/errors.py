class InvalidIndexException(Exception):
    def __init__(self, message: str = ""):
        super(InvalidIndexException, self).__init__(message)
