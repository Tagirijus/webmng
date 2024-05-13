import os
import yaml



class FileController(object):
    """Classf for handling load and save operations."""

    def __init__(self, data_dir=None):
        self.init_data_dir(data_dir)

    def init_data_dir(self, data_dir):
        if data_dir is not None and not os.path.isfile(data_dir):
            self.DATADIR = data_dir
        else:
            self.DATADIR = os.path.join(
                os.path.expanduser("~"),
                '.webmng'
            )
        os.makedirs(self.DATADIR, exist_ok=True)

    def prepare_filename(self, subfolder, name):
        """
        With this method you will get the absolute path
        to the file to save to. Also it will create all
        subfolders, if needed.
        """
        folder = os.path.join(
            self.DATADIR,
            subfolder
        )
        os.makedirs(folder)
        filename = f'{name}.yaml'
        return os.path.join(folder, filename)

    def create_subfolders(self, subfolder):
        os.makedirs(
            os.path.join(self.DATADIR, subfolder),
            exist_ok=True
        )

    def add_yaml_extension(self, filename):
        if filename.lower().endswith('.yaml'):
            return filename
        else:
            return filename.replace('.YAML', '') + '.yaml'

    def create_absolute_filename(self, filename='config', subfolder=None):
        if subfolder is not None:
            return os.path.join(
                self.DATADIR,
                subfolder,
                self.add_yaml_extension(filename)
            )
        else:
            return os.path.join(
                self.DATADIR,
                self.add_yaml_extension(filename)
            )

    def save(self, data, filename='config', subfolder=None):
        """
        filename must not contain the ending. ".yaml" will
        be used by default then.
        Sufolders will be created recursively in the data dir,
        if they do not exist.

        By default filename is "config" and it is supposed
        to store possible configuration of the tool.
        """
        if not isinstance(data, dict):
            raise TypeError('The data argument has to be a dict in FileController.save().')
        if subfolder is not None:
            self.create_subfolders(subfolder)
        with open(self.create_absolute_filename(filename, subfolder), 'w') as myfile:
            yaml.dump(data, myfile, default_flow_style=False)

    def load(self, filename='config', subfolder=None):
        """
        filename must not contain the ending. ".yaml" will
        be used by default then.

        By default filename is "config" and it is supposed
        to store possible configuration of the tool.
        """
        with open(self.create_absolute_filename(filename, subfolder), 'r') as myfile:
            loaded_data = yaml.safe_load(myfile)
        return loaded_data

    def exists(self, filename='config', subfolder=None):
        return os.path.exists(self.create_absolute_filename(filename, subfolder))
