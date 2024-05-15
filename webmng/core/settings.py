"""The class holding all the settings."""

import argparse
import os
import yaml



class Settings(object):
    """Settings class."""

    def __init__(self):
        """Initialize the class."""
        self.DATADIR = os.path.join(os.path.expanduser("~"), '.webmng')
        self.init_arguments()
        self.init_config()

    def default_config(self):
        """Set the default config."""
        # EDITOR
        self.EDITOR = 'vim'

    def overwrite_config(self, config_data):
        if 'EDITOR' in config_data:
            self.EDITOR = config_data['EDITOR']

    def get_config_as_dict(self):
        return {
            'EDITOR': self.EDITOR
        }

    def init_config(self):
        """
        Try to get the user set config and fill missing config
        parts with the default_config() output.
        """
        # first set the default config attributes
        self.default_config()

        # now try to load a config file and replace the respecting configs
        absolute_config_file = os.path.join(self.DATADIR, 'config.yaml')
        if os.path.exists(absolute_config_file):
            with open(absolute_config_file, 'r') as myfile:
                loaded_config_data = yaml.safe_load(myfile)
            self.overwrite_config(loaded_config_data)


    def init_arguments(self):
        self.parser = argparse.ArgumentParser(
            description=(
                'A programm for managing some minor server related things.'
            )
        )

        self.parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')

        # ACTION SUBPARSER

        action_parser = self.parser.add_subparsers(dest='action', help='The action to perform')
        self.action = {}


        ## ADD ACTION WITH SUBPARSER

        self.action['add'] = action_parser.add_parser(
            'add',
            help='Add project type or project',
            description='Add project type or project'
        )
        add_sub = self.action['add'].add_subparsers(
            dest='type',
            help='The type to add: project type or project',
            description='The type to add: project type or project'
        )

        add_sub_type = add_sub.add_parser(
            'type',
            help='Add a project type',
            description='Add a project type'
        )
        add_sub_type.add_argument('name', help='Name of the project type')

        add_sub_project = add_sub.add_parser(
            'project',
            help='Add a project',
            description='Add a project'
        )
        add_sub_project.add_argument('name', help='Name of the project')


        ## EDIT ACTION WITH SUBPARSER

        self.action['edit'] = action_parser.add_parser(
            'edit',
            help='Edit project type or project',
            description='Edit project type or project'
        )
        edit_sub = self.action['edit'].add_subparsers(
            dest='type',
            help='The type to edit: project type or project',
            description='The type to edit: project type or project'
        )

        edit_sub_type = edit_sub.add_parser(
            'type',
            help='Edit a project type',
            description='Edit a project type'
        )
        edit_sub_type.add_argument('name', help='Name of the project type', nargs='?')

        edit_sub_project = edit_sub.add_parser(
            'project',
            help='Edit a project',
            description='Edit a project'
        )
        edit_sub_project.add_argument('name', help='Name of the project', nargs='?')


        ## DELETE ACTION WITH SUBPARSER

        self.action['delete'] = action_parser.add_parser(
            'delete',
            help='Delete project type or project',
            description='Delete project type or project'
        )
        delete_sub = self.action['delete'].add_subparsers(
            dest='type',
            help='The type to delete: project type or project',
            description='The type to delete: project type or project'
        )

        delete_sub_type = delete_sub.add_parser(
            'type',
            help='Delete a project type',
            description='Delete a project type'
        )
        delete_sub_type.add_argument('name', help='Name of the project type', nargs='?')

        delete_sub_project = delete_sub.add_parser(
            'project',
            help='Delete a project',
            description='Delete a project'
        )
        delete_sub_project.add_argument('name', help='Name of the project', nargs='?')


        ## INFO ACTION WITH SUBPARSER

        self.action['info'] = action_parser.add_parser(
            'info',
            help='Get info about project type or project',
            description='Get info about project type or project'
        )
        info_sub = self.action['info'].add_subparsers(
            dest='type',
            help='The type to get info about: project type or project',
            description='The type to get info about: project type or project'
        )

        info_sub_type = info_sub.add_parser(
            'type',
            help='Get info about a project type',
            description='Get info about a project type'
        )
        info_sub_type.add_argument('name', help='Name of the project type', nargs='?')

        info_sub_project = info_sub.add_parser(
            'project',
            help='Get info about a project',
            description='Get info about a project'
        )
        info_sub_project.add_argument('name', help='Name of the project', nargs='?')


        ## COMMANDS FOR A PROJECT

        self.action['start'] = action_parser.add_parser(
            'start',
            help='Start a project',
            description='Start a project'
        )
        self.action['start'].add_argument('name', help='Name of the project')

        self.action['stop'] = action_parser.add_parser(
            'stop',
            help='Stop a project',
            description='Stop a project'
        )
        self.action['stop'].add_argument('name', help='Name of the project')


        # GLOBAL COMMANDS

        self.action['list'] = action_parser.add_parser(
            'list',
            help='List all available project types and projects',
            description='List all available project types and projects'
        )

        self.action['status'] = action_parser.add_parser(
            'status',
            help='Show all project statuses',
            description='Show all project statuses'
        )

        self.action['config'] = action_parser.add_parser(
            'config',
            help='Open programm config in editor',
            description=(
                'By default or when run for the first time this will open'
                + ' the config file in vim.'
            )
        )


        self.ARGS = self.parser.parse_args()

    def print_help_for_action(self):
        self.action[self.ARGS.action].print_help()
