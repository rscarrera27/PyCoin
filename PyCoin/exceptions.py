class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class DBAccessError(Error):
    """Exception raised for errors in the input.

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg


class NodeUnavailableError(Error):

    def __init__(self, msg="Node unavailable"):
        self.msg = msg


class UserNotExistsError(Error):

    def __init__(self, msg="User Not Exists"):
        self.msg = msg