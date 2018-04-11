# -*- coding: utf-8 -*-

"""Tests for the command line of the `dar` package."""

import pytest

from click.testing import CliRunner

from dar.cli import main, register, run


def test_basic_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
    help_result = runner.invoke(main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
