import click
from controller import utils
from model.settings import Settings
from model.webmng import Webmng


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@click.pass_context
# @click.option('-v', '--verbose', is_flag=True, help='Enable verbose mode')
def cli(ctx):
    """
    A programm for managing some minor server related things.

    Primary intended to use with an Apache2 server.
    """
    ctx.obj = Webmng()


@cli.command()
@click.pass_context
@click.argument('name')
def add(ctx, name):
    """Add a new site"""
    ctx.obj.add(name)


@cli.command()
@click.pass_context
@click.argument('name')
def edit(ctx, name):
    """Edit a site"""
    ctx.obj.edit(name)


@cli.command()
@click.pass_context
@click.argument('name')
def delete(ctx, name):
    """Delete a site"""
    ctx.obj.delete(name)


@cli.command()
@click.pass_context
@click.argument('name')
def up(ctx, name):
    """Up / enable a site"""
    ctx.obj.up(name)


@cli.command()
@click.pass_context
@click.argument('name')
def down(ctx, name):
    """Down / disable a site"""
    ctx.obj.down(name)


@cli.command()
def config():
    """
    Open config in editor

    By default or when run for the first time this will open
    the config file in vi.
    """
    S = Settings()
    utils.edit_config()


@cli.command()
@click.pass_context
def list(ctx):
    """List all available sites"""
    ctx.obj.list()


@cli.command()
@click.pass_context
@click.option(
    '-i', '--interval',
    default=60,
    help='The interval in seconds for the MONITOR action. By default it is set to 60.'
)
def monitor(ctx, interval):
    """
    Monitor changes of the sites

    Monitor changes of the sites every N seconds,
    while N can be set with --interval/-i and is
    60 by default. The MONITOR action stays in the
    foreground and makes it suitable to be run via
    pm2, for example.
    """
    ctx.obj.monitor(interval)
