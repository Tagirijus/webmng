"""The class holding all the settings."""

import os
import yaml



class Settings(object):
    """Settings class."""

    def __init__(self):
        """Initialize the class."""
        self.DATADIR = os.path.join(os.path.expanduser("~"), '.webmng')
        self.CONFIGFILE = os.path.join(self.DATADIR, 'config.yaml')
        self.init_config()

    def default_config(self):
        """Set the default config."""
        self.EDITOR = 'vi'
        self.SITES_DIR = '/etc/apache2/sites-available'

    def overwrite_config(self, config_data):
        self.EDITOR = config_data.get('EDITOR', self.EDITOR)
        self.SITES_DIR = config_data.get('SITES_DIR', self.SITES_DIR)

    def get_config_as_dict(self):
        return {
            'EDITOR': self.EDITOR,
            'SITES_DIR': self.SITES_DIR
        }

    def init_config(self):
        """
        Try to get the user set config and fill missing config
        parts with the default_config() output.
        """
        # first set the default config attributes
        self.default_config()

        # now try to load a config file and replace the respecting configs
        if os.path.exists(self.CONFIGFILE):
            with open(self.CONFIGFILE, 'r') as myfile:
                loaded_config_data = yaml.safe_load(myfile)
            self.overwrite_config(loaded_config_data)
