from click.testing import CliRunner
import matplotlib.pyplot as plt
import os
from PIL import Image
import pytest
from unittest import mock

from grafte.cli import cli


@pytest.fixture
def input_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "mydata.csv"
    p.write_text(
        """
name,age
Alice,42
Bob,9
Chaz,101
""".strip()
    )
    return p


@pytest.fixture(autouse=True)
def mock_plt_show():
    with mock.patch.object(plt, "show") as mock_show:
        yield mock_show  # Provide mock_show to tests, in case it's needed


def test_help_option(mock_plt_show):
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output
    assert "Commands" in result.output
    assert "bar" in result.output
    assert "--help " in result.output
    mock_plt_show.assert_not_called()


def test_no_subcommand(mock_plt_show):
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert "Usage:" in result.output
    assert "Commands" in result.output
    assert "bar" in result.output
    assert "--help " in result.output
    mock_plt_show.assert_not_called()


def test_cli_version(mock_plt_show):
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "version" in result.output
    mock_plt_show.assert_not_called()


def test_basic_bar(input_file, mock_plt_show):
    """
    $ grafte bar mydata.csv
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["bar", str(input_file)])
    assert result.exit_code == 0
    mock_plt_show.assert_called_once()


def test_quiet_mode(input_file, mock_plt_show):
    """
    $ grafte bar mydata.csv --quiet
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["bar", str(input_file), "--quiet"])
    assert result.exit_code == 0
    mock_plt_show.assert_not_called()


def test_output_file(input_file, mock_plt_show):
    """
    $ grafte mydata.csv -o mysheet.png
    """
    runner = CliRunner()
    outfile_path = "mydata.png"

    with runner.isolated_filesystem():
        assert not os.path.exists(outfile_path)

        result = runner.invoke(cli, ["bar", str(input_file), "-o", outfile_path])
        assert result.exit_code == 0

        mock_plt_show.assert_called_once()
        assert os.path.exists(outfile_path)


def test_read_from_stdin(input_file, mock_plt_show):
    """
    $ cat mydata.csv | grafte bar -o mysheet.png
    """

    runner = CliRunner()

    with runner.isolated_filesystem():
        outfile_path = "mydata.png"

        with input_file.open("r") as infile:
            result = runner.invoke(
                cli, ["bar", "-o", outfile_path], input=infile.read()
            )

            assert result.exit_code == 0
            mock_plt_show.assert_called_once()
            assert os.path.exists(outfile_path)


@pytest.mark.slow
def test_output_valid_image_formats(input_file):
    runner = CliRunner()
    with runner.isolated_filesystem():

        for fmt in ("png", "jpg", "tiff"):
            outfile_path = f"mydata.{fmt}"

            result = runner.invoke(cli, ["bar", str(input_file), "-o", outfile_path])
            assert result.exit_code == 0

            with Image.open(outfile_path) as img:
                expected_fmt = "JPEG" if fmt == "jpg" else fmt.upper()
                assert (
                    img.format == expected_fmt
                ), f"{outfile_path} must be valid {expected_fmt}"
