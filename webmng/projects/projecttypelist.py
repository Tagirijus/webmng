import os
from webmng.core.base import Base
from webmng.projects.projecttype import ProjectType


class ProjectTypeList(Base):
    """The class for listing all available project types"""

    def __init__(self, settings):
        super().__init__(settings)
        self.FOLDER = os.path.join(self.SETTINGS.DATADIR, 'projecttypes')
        self.init_list()

    def init_list(self):
        self.LIST = []
        for root, dirs, files in os.walk(self.FOLDER):
            for file in files:
                if file.endswith('.yaml'):
                    data = self.FILECONTROLLER.load(file, 'projecttypes')
                    PT = ProjectType()
                    PT.from_dict(data)
                    self.LIST.append(PT)

    def get_list(self):
        return self.LIST
