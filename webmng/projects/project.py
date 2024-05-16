from webmng.projects.projecttype import ProjectType


class Project(object):
    """Base for a webmng project"""

    # Class attributes

    STATUS_RUNNING = 3
    STATUS_STOPPED = 2
    STATUS_INTERRUPTED = 1
    STATUS_ERROR = 0


    # Class methods

    def __init__(self, name='', projecttype=None):
        self.NAME = name
        if projecttype is None:
            self.PROJECTTYPE = ProjectType()
        else:
            self.PROJECTTYPE = projecttype

    def __str__(self):
        return self.get_name()

    def from_dict(self, dic):
        # TODO
        pass

    def to_dict(self):
        return {
            'NAME': self.NAME,
            'PROJECTTYPE': self.PROJECTTYPE.get_name()
        }

    def get_name(self):
        return self.NAME

    def get_projecttype(self) -> str:
        """
        This method will return the type string
        for the project.
        """
        return self.PROJECTTYPE

    def get_status(self, verbose=False) -> int:
        """
        This method will return the status of the project.

        Status codes are defined as class attributes above in
        this abstract class.
        """
        return self.PROJECTTYPE.get_status(verbose)

    def start(self, verbose=False) -> bool:
        """
        This method will start a project.

        Returns True, if executed without errors.
        """
        return self.PROJECTTYPE.start(verbose)

    def stop(self, verbose=False) -> bool:
        """
        This method will stop a project.

        Returns True, if executed without errors.
        """
        return self.PROJECTTYPE.stop(verbose)
