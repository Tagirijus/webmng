"""The class holding all the settings."""

import argparse



class Settings(object):
    """Settings class."""

    def __init__(self):
        """Initialize the class."""
        self.initArguments()

    def initArguments(self):
        self.parser = argparse.ArgumentParser(
            description=(
                'A programm for managing some minor server related things.'
            )
        )

        self.parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')
        self.parser.add_argument('-d', '--data-dir', help='Set a different data directory than ~/.webmng')

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


        ## START AND STOP AND LIST COMMANDS

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


        self.args = self.parser.parse_args()

    def print_help_for_action(self):
        self.action[self.args.action].print_help()
