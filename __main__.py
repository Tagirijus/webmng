"""
A programm for managing some minor server related things.

Author: Manuel Senfft (www.tagirijus.de)
"""

from webmng.settings import Settings
from webmng.webmng import Webmng



def main(settings):
    """Run the programm."""
    webmng = Webmng(settings)
    webmng.run()


if __name__ == '__main__':
    main(Settings())
