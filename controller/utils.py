import os
import subprocess
from model.settings import Settings
from view import printing as p
import yaml


def open_in_editor(filename):
    S = Settings()

    p.print_info(
        f'Opening "{filename}"'
        + f' with "{S.EDITOR}" ...'
    )

    subprocess.run([S.EDITOR, filename])


def save_dict(data, filename):
    if not isinstance(data, dict):
        raise TypeError('The data argument has to be a dict in controller.utils.save_dict().')
    os.makedirs(
        os.path.dirname(filename),
        exist_ok=True
    )
    with open(filename, 'w') as myfile:
        yaml.dump(data, myfile, default_flow_style=False)


def edit_config():
    S = Settings()

    # probably for the first time, create the config file
    if not os.path.exists(S.CONFIGFILE):
        s.print_info(f'Creating default "config" at "{S.DATADIR}/" ...')
    # then save it, yet also save it eveytime to fill new attributes, which
    # were added later in the development
    save_dict(S.get_config_as_dict(), S.CONFIGFILE)
    # now load it
    open_in_editor(S.CONFIGFILE)