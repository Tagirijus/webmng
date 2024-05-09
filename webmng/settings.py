"""The class holding all the settings."""

import argparse


class Settings(object):
    """Settings class."""

    def __init__(
        self
    ):
        """Initialize the class and hard code defaults, if no file is given."""
        self.initArguments()

    def initArguments(self):
        self.args = argparse.ArgumentParser(
            description=(
                'A programm.'
            )
        )

        self.args.add_argument(
            'file',
            help=(
                'a file'
            )
        )

        self.args.add_argument(
            '-v',
            '--verbose',
            action='store_true',
            help='verbose enabled'
        )

        self.args.add_argument(
            '-d',
            '--default',
            default=None,
            help='default parameter'
        )

        self.args = self.args.parse_args()
