# -*- coding: utf-8 -*-

"""Console script for dar."""
import sys
import click

from dar import dar


@click.group()
def main(args=None):
    """Dar is a command line toolbelt for managing different project workflows. """


@main.command()
@click.argument("key")
@click.argument("command", nargs=-1)
def register(key, command):
    config = dar.get_config()
    command = " ".join(command)
    dar.register_alias(config, key, command)


@main.command()
@click.argument("key")
def run(key):
    config = dar.get_config()
    dar.call_alias(config, key)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
