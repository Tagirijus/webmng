from webmng.core.filecontroller import FileController


class Base(object):
    """
    The base class, which will initialize certain base
    attributes for a class. These are for example:

    self.SETTINGS
        the settings object
    self.ARGS
        the args of the settings object
    self.FILECONTROLLER
        the file controller object

    """

    def __init__(self, settings):
        self.SETTINGS = settings
        self.ARGS = settings.ARGS
        self.FILECONTROLLER = FileController(settings.DATADIR)
