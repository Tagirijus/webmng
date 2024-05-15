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
            self.add('projecttypes')

        # project
        elif self.ARGS.type == 'project':
            self.add('projects')

        # fallback: print help
        else:
            self.SETTINGS.print_help_for_action()

    def add(self, subfolder):
        PT = ProjectType(self.ARGS.name)
        if self.FILECONTROLLER.exists(self.ARGS.name, subfolder):
            print(Fore.RED + f'"{self.ARGS.name}" already exists at "{subfolder}/".')
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
            print(Fore.BLUE + f'Saving "{self.ARGS.name}" at "{subfolder}/" ...')
            self.FILECONTROLLER.save(data, self.ARGS.name, subfolder)
            print(Fore.BLUE + f'Opening "{self.ARGS.name}" at "{subfolder}/" with "{self.SETTINGS.EDITOR}" ...')
            subprocess.run([self.SETTINGS.EDITOR, self.FILECONTROLLER.create_absolute_filename(self.ARGS.name, subfolder)])



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
        print('edit project type ...')

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
        print(Fore.BLUE + f'Opening "config" at "{self.SETTINGS.DATADIR}/" with "{self.SETTINGS.EDITOR}" ...')
        subprocess.run([self.SETTINGS.EDITOR, self.FILECONTROLLER.create_absolute_filename()])
