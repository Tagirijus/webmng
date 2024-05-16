"""
This script contains templates of project types and a list
with all of these so that the user gets a selectable choice
list, when they want to add a new project type.

In the respecting commands etc. there are the following possible
placeholders:

%NAME%:     The name of the project.
"""

class Templates(object):

    def __init__(self):
        """
        This class attributes are there to be safe
        that for the template returning the dict
        keys do exist. I am not sure, if there
        would be a more clever way to have some
        kind of soft-interface, technically.
        """
        self.START_COMMAND = ''
        self.STOP_COMMAND = ''
        self.STATUS_COMMAND = ''
        self.STATUS_REGEX = r''

    def get(self):
        """
        Gets the class attributes and return them in a dict.
        """
        return {
            'START_COMMAND': self.START_COMMAND,
            'STOP_COMMAND': self.STOP_COMMAND,
            'STATUS_COMMAND': self.STATUS_COMMAND,
            'STATUS_REGEX': self.STATUS_REGEX
        }

    def get_list(self):
        return {
            'empty': self.empty(),
            'docker': self.docker(),
            'apachesite': self.apachesite()
        }

    def empty(self):
        """
        An empty template for a project.
        """
        self.START_COMMAND = ''
        self.STOP_COMMAND = ''
        self.STATUS_COMMAND = ''
        self.STATUS_REGEX = r''
        return self.get()

    def docker(self):
        """
        TODO

        The template for a docker project.
        """
        self.START_COMMAND = 'echo "starting docker %NAME%"'
        self.STOP_COMMAND = 'echo "stopping docker %NAME%"'
        self.STATUS_COMMAND = 'echo "getting docker status for %NAME% - okay?"'
        self.STATUS_REGEX = r'\bokay\?\b'
        return self.get()

    def apachesite(self):
        """
        TODO

        The template for an apache site project.
        """
        self.START_COMMAND = 'echo "starting apachesite %NAME%"'
        self.STOP_COMMAND = 'echo "stopping apachesite %NAME%"'
        self.STATUS_COMMAND = 'echo "getting apachesite status for %NAME% - okay?"'
        self.STATUS_REGEX = r'\bokay\?\b'
        return self.get()
