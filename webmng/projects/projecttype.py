class ProjectType(object):
    """Base type for a project"""

    def __init__(
        self, name, start_command=None, stop_command=None, status_command=None, status_regex=None
    ):
        self.NAME = name
        self.START_COMMAND = start_command
        self.STOP_COMMAND = stop_command
        self.STATUS_COMMAND = status_command
        self.STATUS_REGEX = status_regex

    def __str__(self):
        return str(self.NAME)

    def get_status(self, verbose=False):
        pass

    def start(self, verbose=False):
        pass

    def stop(self, verbose=False):
        pass
