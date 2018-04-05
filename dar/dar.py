# -*- coding: utf-8 -*-

"""Main module."""
from configparser import ConfigParser
import subprocess
from pathlib import Path


def register_alias(config: ConfigParser, key: str, command: str):
    """Register a new alias in the given configuration
    Args:
        config (ConfigParser): The configuration to write the alias to.
        key (str): The shorthand that will be registered.
        command (str): The actual command that needs to be ran.
    """
    # Create the new section for that alias
    config[key] = {}
    # Populate it with the command
    config.set(key, " ".join(command))
    with open(".darconfig", "w", encoding="utf-8") as config_file:
        config.write(config_file)


def call_alias(config: ConfigParser, key: str):
    """Run the command specified at the alias
    Args:
        config (ConfigParser): The configuration to read the alias from.
        key (str): The shorthand to look up and run
    """
    try:
        commands = config[key]
    except KeyError:
        raise ValueError(f"Alias {key} is not set")

    for command in commands.keys():
        print(f'Running: {command}')
        subprocess.run(command.split(" "))


def get_config(path="./", filename=".darconfig"):
    config = ConfigParser(allow_no_value=True)
    config_path = Path(path) / filename
    try:
        with open(config_path, "r") as config_file:
            config.read_file(config_file)
    except FileNotFoundError:
        print("Dar configuration file not found, creating one...")
        pass
    return config
