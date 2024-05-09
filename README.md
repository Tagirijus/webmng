A programm for managing some minor server related things.

# Description

Here I try to write down my initial idea before I start to code. I might change the text later.

With this programm I wanted to code my own very easy _server monitoring and managing_ programm. I know that there are certain server monitoring tools. Yet a) I have not much experience with servers so far and b) I wanted a very ultra easy and basic tool, where I know what it does and why.

The initial idea basically is for this tool to be able to:

- list which kind of web server projects are running and what their status is _(e.g. docker container or apache routes, etc.)_
- being able to start or stop a project _(e.g. starting a docker container, or enablign/disabling a apache site)_
- being able to set up subdomains based on a template

The list should be a color coded and easy to read list where I can see, summarized, what the status of projects are. Also it should be able to show, if e.g. some docker containers were stopped unexpected or so.

Underlying I imagine that this programm mainly is based rather on some kind of scripts. The idea might change during the coding process, not sure. The idea behind all this is that I do not want to have differnet places and remember different commands to see how my web projects are running. Instead I want just one tool to rule certain differnet things. Then I know how to start the programm and the commands / arguments are always the same, despite the kind of project typ (docker container, apache site, maybe nodeJS project at some point, etc.).

I plan to make this whole tool open source and public. Let's see where the journey will lead me.

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
