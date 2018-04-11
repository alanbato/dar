# -*- coding: utf-8 -*-

"""Tests for the command line of the `dar` package."""

import pytest

from click.testing import CliRunner

import dar.cli as cli


def test_basic_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
