# -*- coding: utf-8 -*-

"""Tests for the main module of the `dar` package."""
import os

import pytest
from pretend import call_recorder, call

from dar.dar import register_alias, call_alias, get_config


@pytest.fixture(name="config_file", scope="function")
def config_file(request):
    yield get_config()

    try:
        os.remove(".darconfig")
    except FileNotFoundError:
        pass


def test_register_alias(config_file):
    alias = "tests"
    command = "pytest /path/to/tests"
    register_alias(config_file, alias, command)

    assert config_file.has_section(alias)
    assert config_file.has_option(alias, command)


def test_call_alias(config_file):
    alias = "tests"
    command = "pytest /path/to/tests"
    config_file.add_section(alias)
    config_file.set(alias, command)
    call_alias = call_recorder(lambda x, y, z: (y, z))
    call_alias(config_file, alias, command)

    assert call_alias.calls == [call(config_file, alias, command)]


def test_get_config_no_file():
    try:
        os.remove(".darconfig")
    except FileNotFoundError:
        pass
    config = get_config()
    assert len(config.items()) == 1
    assert len(config["DEFAULT"]) == 0
