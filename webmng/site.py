"""
This class generates a Site object from the given
Apache 2 conf file!
"""

import os


class Site(object):

    def __init__(self, filename):
        self.FILENAME_ABSOLUTE = filename
        self.FILENAME = os.path.basename(self.FILENAME_ABSOLUTE)
        self.NAME = os.path.splitext(self.FILENAME)[0]
        self.SITES_DIR = os.path.dirname(self.FILENAME_ABSOLUTE)
        self.SITES_DIR_ENABLED = self.SITES_DIR.replace('sites-available', 'sites-enabled')

        self.CONTENT = self.init_content()
        self.DOMAIN = self.init_domain()
        self.PORT = self.init_port()

    def __str__(self):
        is_up = 'up' if self.is_up() else 'down'
        return f'{self.get_name()} --> {self.get_domain()}:{self.get_port()} [{is_up}]'

    def init_content(self):
        out = ''
        with open(self.FILENAME_ABSOLUTE, 'r') as myfile:
            out = myfile.read()
        return out

    def init_domain(self):
        # TODO
        # fetch domain from *.conf file with regex or so
        return 'todo.de'

    def init_port(self):
        # TODO
        # fetch port from *.conf file with regex or so
        return '3000'


    def is_up(self):
        for filename in os.listdir(self.SITES_DIR_ENABLED):
            if filename == self.FILENAME:
                return True
        return False


    def get_name(self):
        return self.NAME

    def get_domain(self):
        return self.DOMAIN

    def get_port(self):
        return self.PORT
