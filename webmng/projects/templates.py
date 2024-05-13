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
        self.start_command = ''
        self.stop_command = ''
        self.status_command = ''
        self.status_regex = r''

    def get(self):
        """
        Gets the class attributes and return them in a dict.
        """
        return {
            'start_command': self.start_command,
            'stop_command': self.stop_command,
            'status_command': self.status_command,
            'status_regex': self.status_regex
        }

    def list(self):
        return {
            'empty': self.empty(),
            'docker': self.docker(),
            'apachesite': self.apachesite()
        }

    def empty(self):
        """
        An empty template for a project.
        """
        return self.get()

    def docker(self):
        """
        TODO

        The template for a docker project.
        """
        self.start_command = 'echo "starting docker %NAME%"'
        self.stop_command = 'echo "stopping docker %NAME%"'
        self.status_command = 'echo "getting docker status for %NAME% - okay?"'
        self.status_regex = r'\bokay\?\b'
        return self.get()

    def apachesite(self):
        """
        TODO

        The template for an apache site project.
        """
        self.start_command = 'echo "starting apachesite %NAME%"'
        self.stop_command = 'echo "stopping apachesite %NAME%"'
        self.status_command = 'echo "getting apachesite status for %NAME% - okay?"'
        self.status_regex = r'\bokay\?\b'
        return self.get()
