import os
from model.settings import Settings
from model.site import Site
import yaml



class Webmng(object):
    """Class for controlling the logic flow of the programm."""

    def __init__(self):
        self.SITES = None

    def get_sites(self):
        if self.SITES is None:
            S = Settings()
            self.SITES = []
            for filename in os.listdir(S.SITES_DIR):
                if filename.lower().endswith('.conf'):
                    conf_filename = os.path.join(S.SITES_DIR, filename)
                    self.SITES.append(Site(conf_filename))
        return self.SITES


    def add(self, name):
        print(f'Add site "{name}" ...')


    def edit(self):
        print('Edit site ...')


    def delete(self):
        print('Delete site ...')


    def up(self):
        print('Up / enable site ...')


    def down(self):
        print('Down / disable site ...')


    def list(self):
        print('Listing sites ...')
        for site in self.get_sites():
            print(site)


    def monitor(self, interval = 60):
        print('Showing sites statuses ...')
