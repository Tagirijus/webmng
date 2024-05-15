from colorama import Fore, Back, Style
import subprocess
from webmng.core.filecontroller import FileController
from webmng.projects.project import Project
from webmng.projects.projecttype import ProjectType
from webmng.projects.templates import Templates



class Webmng(object):
    """Class for controlling the logic flow of the programm."""

    def __init__(self, settings):
        self.SETTINGS = settings
        self.ARGS = settings.ARGS
        self.FILECONTROLLER = FileController(settings.DATADIR)

    def open_in_editor(self, name, subfolder=None):
        absolute_filename = self.FILECONTROLLER.create_absolute_filename(name, subfolder)
        print(
            Fore.BLUE
            + f'Opening "{absolute_filename}"'
            + f' with "{self.SETTINGS.EDITOR}" ...'
        )
        subprocess.run([self.SETTINGS.EDITOR, absolute_filename])



    def run(self):
        # ACTION "ADD"
        if self.ARGS.action == 'add':
            self.action_add()


        # ACTION "EDIT"
        elif self.ARGS.action == 'edit':
            self.action_edit()


        # ACTION "DELETE"
        elif self.ARGS.action == 'delete':
            self.action_delete()


        # ACTION "INFO"
        elif self.ARGS.action == 'info':
            self.action_info()


        # ACTION "START"
        elif self.ARGS.action == 'start':
            self.action_start()


        # ACTION "STOP"
        elif self.ARGS.action == 'stop':
            self.action_stop()


        # ACTION "LIST"
        elif self.ARGS.action == 'list':
            self.action_list()


        # ACTION "STATUS"
        elif self.ARGS.action == 'status':
            self.action_status()


        # ACTION "CONFIG"
        elif self.ARGS.action == 'config':
            self.action_config()


        # fallback: print help
        else:
            self.SETTINGS.parser.print_help()



    def action_add(self):
        # project type
        if self.ARGS.type == 'type':
            self.add_type()

        # project
        elif self.ARGS.type == 'project':
            self.add_project()

        # fallback: print help
        else:
            self.SETTINGS.print_help_for_action()

    def add_type(self):
        if self.FILECONTROLLER.exists(self.ARGS.name, 'projecttypes'):
            print(Fore.RED + f'"{self.ARGS.name}" already exists at "projecttypes/".')
            exit()
        else:
            T = Templates()
            LIST = T.list()
            print(Fore.RESET + 'Choose from the following templates:')
            i = 1
            choices = {}
            for template in LIST:
                print(Fore.YELLOW + f'({i})' + Fore.RESET + f' {template}')
                choices[str(i)] = template
                i += 1
            user = input('> ')
            if user.lower() in ['q', 'quit', 'exit', 'cancel']:
                print(Fore.RESET + 'Cancelling ...')
                exit()
            if user not in choices:
                user = '1'
            print(Fore.BLUE + f'"{choices[user]}" was chosen. Getting the data ...')
            data = LIST[choices[user]]
            print(Fore.BLUE + f'Saving "{self.ARGS.name}" at "projecttypes/" ...')
            self.FILECONTROLLER.save(data, self.ARGS.name, 'projecttypes')
            self.open_in_editor(self.ARGS.name, 'projecttypes')

    def add_project(self):
        if self.FILECONTROLLER.exists(self.ARGS.name, 'projects'):
            print(Fore.RED + f'"{self.ARGS.name}" already exists at "projects/".')
            exit()
        else:
            # TODO:
            # - project types auflisten und wählen
            T = Templates()
            LIST = T.list()
            print(Fore.RESET + 'Choose from the following templates:')
            i = 1
            choices = {}
            for template in LIST:
                print(Fore.YELLOW + f'({i})' + Fore.RESET + f' {template}')
                choices[str(i)] = template
                i += 1
            user = input('> ')
            if user.lower() in ['q', 'quit', 'exit', 'cancel']:
                print(Fore.RESET + 'Cancelling ...')
                exit()
            if user not in choices:
                user = '1'
            print(Fore.BLUE + f'"{choices[user]}" was chosen. Getting the data ...')
            data = LIST[choices[user]]
            print(Fore.BLUE + f'Saving "{self.ARGS.name}" at "projects/" ...')
            self.FILECONTROLLER.save(data, self.ARGS.name, 'projects')
            self.open_in_editor(self.ARGS.name, 'projects')



    def action_edit(self):
        # project type
        if self.ARGS.type == 'type':
            self.edit_type()

        # project
        elif self.ARGS.type == 'project':
            self.edit_project()

        # fallback: print help
        else:
            self.SETTINGS.print_help_for_action()

    def edit_type(self):
        if not self.FILECONTROLLER.exists(self.ARGS.name, 'projecttypes'):
            print(Fore.RED + f'Project type "{self.ARGS.name}" does not exist.')
            exit()
        else:
            self.open_in_editor(self.ARGS.name, 'projecttypes')

    def edit_project(self):
        print('edit project ...')


    def action_delete(self):
        # project type
        if self.ARGS.type == 'type':
            self.delete_type()

        # project
        elif self.ARGS.type == 'project':
            self.delete_project()

        # fallback: print help
        else:
            self.SETTINGS.print_help_for_action()

    def delete_type(self):
        print('delete project type ...')

    def delete_project(self):
        print('delete project ...')


    def action_info(self):
        # project type
        if self.ARGS.type == 'type':
            self.info_type()

        # project
        elif self.ARGS.type == 'project':
            self.info_project()

        # fallback: print help
        else:
            self.SETTINGS.print_help_for_action()

    def info_type(self):
        print('show project type info ...')

    def info_project(self):
        print('show project info ...')


    def action_start(self):
        print(f'Starting {self.ARGS.name} ...')


    def action_stop(self):
        print(f'Stopping {self.ARGS.name} ...')


    def action_list(self):
        print('Listing projects ...')


    def action_status(self):
        print('Showing project statuses ...')


    def action_config(self):
        # probably for the first time, create the config file
        if not self.FILECONTROLLER.exists():
            print(Fore.BLUE + f'Creating default "config" at "{self.SETTINGS.DATADIR}/" ...')
            self.FILECONTROLLER.save(self.SETTINGS.get_config_as_dict())
        # now load it
        self.open_in_editor('config')
