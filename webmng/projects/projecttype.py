class ProjectType(object):
    """Base type for a project"""

    def __init__(
        self, name='', start_command='', stop_command='', status_command='', status_regex=''
    ):
        # NAME is the name of the project
        self.NAME = name

        # the commands to call to do stuff for the project
        self.START_COMMAND = start_command
        self.STOP_COMMAND = stop_command
        self.STATUS_COMMAND = status_command
        self.STATUS_REGEX = status_regex

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return self.NAME

    def from_dict(self, dic):
        self.NAME = dic.get('NAME', self.NAME)
        self.START_COMMAND = dic.get('START_COMMAND', self.START_COMMAND)
        self.STOP_COMMAND = dic.get('STOP_COMMAND', self.STOP_COMMAND)
        self.STATUS_COMMAND = dic.get('STATUS_COMMAND', self.STATUS_COMMAND)
        self.STATUS_REGEX = dic.get('STATUS_REGEX', self.STATUS_REGEX)

    def to_dict(self):
        return {
            'NAME': self.NAME,
            'START_COMMAND': self.START_COMMAND,
            'STOP_COMMAND': self.STOP_COMMAND,
            'STATUS_COMMAND': self.STATUS_COMMAND,
            'STATUS_REGEX': self.STATUS_REGEX
        }

    def get_status(self, verbose=False):
        pass

    def start(self, verbose=False):
        pass

    def stop(self, verbose=False):
        pass
