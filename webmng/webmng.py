from colorama import Fore, Back, Style
import os
import subprocess
from webmng.site import Site
import yaml



class Webmng(object):
    """Class for controlling the logic flow of the programm."""

    def __init__(self, settings):
        self.SETTINGS = settings
        self.ARGS = settings.ARGS
        self.SITES = None

    def open_in_editor(self, filename):
        print(
            Fore.BLUE
            + f'Opening "{filename}"'
            + f' with "{self.SETTINGS.EDITOR}" ...'
        )
        subprocess.run([self.SETTINGS.EDITOR, filename])

    def save_dict(self, data, filename):
        if not isinstance(data, dict):
            raise TypeError('The data argument has to be a dict in webmng.save_dict().')
        os.makedirs(
            os.path.dirname(filename),
            exist_ok=True
        )
        with open(filename, 'w') as myfile:
            yaml.dump(data, myfile, default_flow_style=False)

    def get_sites(self):
        if self.SITES is None:
            self.SITES = []
            for filename in os.listdir(self.SETTINGS.SITES_DIR):
                if filename.lower().endswith('.conf'):
                    conf_filename = os.path.join(self.SETTINGS.SITES_DIR, filename)
                    self.SITES.append(Site(conf_filename))
        return self.SITES



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


        # ACTION "UP"
        elif self.ARGS.action == 'up':
            self.action_up()


        # ACTION "DOWN"
        elif self.ARGS.action == 'down':
            self.action_down()


        # ACTION "CONFIG"
        elif self.ARGS.action == 'config':
            self.action_config()


        # ACTION "LIST"
        elif self.ARGS.action == 'list':
            self.action_list()


        # ACTION "MONITOR"
        elif self.ARGS.action == 'monitor':
            self.action_monitor()


        # fallback: print help
        else:
            self.SETTINGS.parser.print_help()



    def action_add(self):
        print('Add site ...')


    def action_edit(self):
        print('Edit site ...')


    def action_delete(self):
        print('Delete site ...')


    def action_up(self):
        print('Up / enable site ...')


    def action_down(self):
        print('Down / disable site ...')


    def action_config(self):
        # probably for the first time, create the config file
        if not os.path.exists(self.SETTINGS.CONFIGFILE):
            print(Fore.BLUE + f'Creating default "config" at "{self.SETTINGS.DATADIR}/" ...')
        # then save it, yet also save it eveytime to fill new attributes, which
        # were added later in the development
        self.save_dict(self.SETTINGS.get_config_as_dict(), self.SETTINGS.CONFIGFILE)
        # now load it
        self.open_in_editor(self.SETTINGS.CONFIGFILE)


    def action_list(self):
        print('Listing sites ...')
        for site in self.get_sites():
            print(site)


    def action_monitor(self):
        print('Showing sites statuses ...')
