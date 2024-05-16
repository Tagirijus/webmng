import os
from webmng.core.base import Base
from webmng.projects.projecttype import ProjectType


class Project(Base):
    """Project for webmng"""

    # Class attributes, which won't be saved

    STATUS_RUNNING = 3
    STATUS_STOPPED = 2
    STATUS_INTERRUPTED = 1
    STATUS_ERROR = 0


    # Class methods

    def __init__(self, settings, name='', projecttype=None):
        super().__init__(settings)
        self.NAME = name
        self.PROJECTTYPE = ProjectType()
        if isinstance(projecttype, ProjectType):
            self.PROJECTTYPE = projecttype
        else:
            self.load_projecttype(projecttype)

    def __str__(self):
        return self.get_name()

    def load_projecttype(self, projecttypename):
        if os.path.exists(self.FILECONTROLLER.create_absolute_filename(str(projecttypename), 'projecttypes')):
            dic = self.FILECONTROLLER.load(projecttypename, 'projecttypes')
            PT = ProjectType()
            PT.from_dict(dic)
            self.PROJECTTYPE = PT

    def from_dict(self, dic):
        self.NAME = dic.get('NAME', self.NAME)
        if 'PROJECTTYPE' in dic:
            self.load_projecttype(dic['PROJECTTYPE'])

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
