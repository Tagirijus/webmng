"""
A programm for managing some minor server related things.

Author: Manuel Senfft (www.tagirijus.de)
"""

from webmng.core.settings import Settings
from webmng.core.webmng import Webmng



def main(settings):
    """Run the programm."""
    webmng = Webmng(settings)
    webmng.run()


if __name__ == '__main__':
    main(Settings())
