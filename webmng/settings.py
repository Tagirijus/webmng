"""The class holding all the settings."""

import argparse
import os
import yaml



class Settings(object):
    """Settings class."""

    def __init__(self):
        """Initialize the class."""
        self.DATADIR = os.path.join(os.path.expanduser("~"), '.webmng')
        self.CONFIGFILE = os.path.join(self.DATADIR, 'config.yaml')
        self.init_arguments()
        self.init_config()

    def default_config(self):
        """Set the default config."""
        self.EDITOR = 'vim'
        self.SITESAVAILABLEDIR = '/etc/apache2/sites-available'
        self.SITESENABLEDDIR = '/etc/apache2/sites-enabled'

    def overwrite_config(self, config_data):
        self.EDITOR = config_data.get('EDITOR', self.EDITOR)
        self.SITESAVAILABLEDIR = config_data.get('SITESAVAILABLEDIR', self.SITESAVAILABLEDIR)
        self.SITESENABLEDDIR = config_data.get('SITESENABLEDDIR', self.SITESENABLEDDIR)

    def get_config_as_dict(self):
        return {
            'EDITOR': self.EDITOR,
            'SITESAVAILABLEDIR': self.SITESAVAILABLEDIR,
            'SITESENABLEDDIR': self.SITESENABLEDDIR
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


    def init_arguments(self):
        self.parser = argparse.ArgumentParser(
            description=(
                'A programm for managing some minor server related things.'
            )
        )

        self.parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')
        self.parser.add_argument(
            '-i', '--interval', default=60,
            help=(
                'The interval in seconds for the MONITOR action. By default it is set to 60.'
            )
        )

        # ACTION SUBPARSER

        action_parser = self.parser.add_subparsers(dest='action', help='The action to perform')
        self.action = {}


        ## SITE ACTIONS

        self.action['add'] = action_parser.add_parser(
            'add',
            help='Add a new site',
            description='Add a new site'
        )
        self.action['add'].add_argument('name', help='Name of the site')

        self.action['edit'] = action_parser.add_parser(
            'edit',
            help='Edit a site',
            description='Edit a site'
        )
        self.action['edit'].add_argument('name', help='Name of the site')

        self.action['delete'] = action_parser.add_parser(
            'delete',
            help='Delete a site',
            description='Delete a site'
        )
        self.action['delete'].add_argument('name', help='Name of the site')

        self.action['up'] = action_parser.add_parser(
            'up',
            help='Enable a site',
            description='Enable a site'
        )
        self.action['up'].add_argument('name', help='Name of the site')

        self.action['down'] = action_parser.add_parser(
            'down',
            help='Disable a site',
            description='Disable a site'
        )
        self.action['down'].add_argument('name', help='Name of the site')



        # GLOBAL COMMANDS

        self.action['config'] = action_parser.add_parser(
            'config',
            help='Open config in editor',
            description=(
                'By default or when run for the first time this will open'
                + ' the config file in vim.'
            )
        )

        self.action['list'] = action_parser.add_parser(
            'list',
            help='List all available sits',
            description='List all available sites'
        )

        self.action['monitor'] = action_parser.add_parser(
            'monitor',
            help=(
                'Monitor changes of the sites every N seconds, while N'
                + ' can be set with --interval/-i and is 60 by default.'
                + ' The MONITOR action stays in the foreground and makes'
                + ' it suitable to be run via pm2, for example.'
            ),
            description=(
                'Monitor changes of the sites every N seconds, while N'
                + ' can be set with --interval/-i and is 60 by default.'
                + ' The MONITOR action stays in the foreground and makes'
                + ' it suitable to be run via pm2, for example.'
            )
        )


        self.ARGS = self.parser.parse_args()

    def print_help_for_action(self):
        self.action[self.ARGS.action].print_help()
