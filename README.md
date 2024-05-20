A programm for managing some minor server related things.

# Description

First of all: I am a total noob and probably coded something in a waste of hours for some really minor task.

This programm is for creating, enabling, disabling and somehow even "monitor" Apache2 server sites. You will be able to add new sites, enable them, disable them or delete them. Then there is the monitoring mode, which will stay alive in the foreground and list changes in the `/etc/apache2/sites-enabled` folder every N seconds. The plan is that this will make the tool suitable for [pm2](https://pm2.keymetrics.io/) (hopefully ...). Did I mention that I am a total noob?

# Installation

I tried to set up a `setup.py`, which should serve as an installation tool or so. According to my rough and noobish research, you have to navigate to this repo (which you could e.g. clone locally) and execute `pip install .`. I guess then it might be possible to start the programm with `python3 -m webmng` - not sure though and at this point this README should read like a joke. Sorry, dear experienced Python people! :D

Another option would be (and this would rather be the noobish option I would consider, since I lack of time and patience to test the setup.py option at the moment): starting the script with `python3 __main__.py` and the respecting parameters. I would set up an alias for this tool in e.g. my _.bashrc_ with _"alias webmng='python3 path_to_repo/__main__.py'"_. And then I could start the programm with `webmng` from the terminal. If the _setup.py_ option works as I wrote, you also might be able to set up an alias for the command `python3 -m webmng`, not sure.

The more I write down, the more noobish I feel. :D

# Usage

I assume that you can start the programm with just entering `webmng` into your terminal. Then you have the option to start it with the help parameter: `webmng -h`. This will list all the options with which you can start the programm.

As long as the tool is not that complex or there will be user feedback (like github issues or so), I won't update this README with every parameter. I hope the `-h` option will give enough info already.

# To do

- Code the programm!

# Changelog

The changelog [is here: CHANGELOG.md](CHANGELOG.md).
