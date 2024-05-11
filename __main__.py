"""
A programm for managing some minor server related things.

Author: Manuel Senfft (www.tagirijus.de)
"""

from webmng.core.settings import Settings
from webmng.projects.project import Project
from webmng.projects.projecttype import ProjectType




def action_add(settings):
    # project type
    if settings.args.type == 'type':
        print('project type adden ...')

    # project
    elif settings.args.type == 'project':
        print('project adden ...')

    # fallback: print help
    else:
        settings.print_help_for_action()


def action_edit(settings):
    # project type
    if settings.args.type == 'type':
        print('project type edit ...')

    # project
    elif settings.args.type == 'project':
        print('project edit ...')

    # fallback: print help
    else:
        settings.print_help_for_action()


def action_delete(settings):
    # project type
    if settings.args.type == 'type':
        print(f'project type delete ...')

    # project
    elif settings.args.type == 'project':
        print('project delete ...')

    # fallback: print help
    else:
        settings.print_help_for_action()


def action_info(settings):
    # project type
    if settings.args.type == 'type':
        print(f'project type info ...')

    # project
    elif settings.args.type == 'project':
        print('project info ...')

    # fallback: print help
    else:
        settings.print_help_for_action()




def main(settings):
    """Run the programm."""

    # ACTION "ADD"
    if settings.args.action == 'add':
        action_add(settings)


    # ACTION "EDIT"
    elif settings.args.action == 'edit':
        action_edit(settings)


    # ACTION "DELETE"
    elif settings.args.action == 'delete':
        action_delete(settings)


    # ACTION "INFO"
    elif settings.args.action == 'info':
        action_info(settings)


    # ACTION "START"
    elif settings.args.action == 'start':
        print(f'Starting {settings.args.name} ...')


    # ACTION "STOP"
    elif settings.args.action == 'stop':
        print(f'Stopping {settings.args.name} ...')


    # ACTION "LIST"
    elif settings.args.action == 'list':
        print(f'Listing projects ...')


    # ACTION "STATUS"
    elif settings.args.action == 'status':
        print(f'Showing project statuses ...')


    # fallback: print help
    else:
        settings.parser.print_help()


if __name__ == '__main__':
    main(Settings())
