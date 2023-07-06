from pro_filer.actions.main_actions import show_details  # NOQA
from unittest.mock import Mock, patch
import time
import datetime

date = "2023-07-05"
ts = time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple())


def test_show_details_when_the_file_does_not_exist(capsys):
    mock_exists = Mock(return_value=False)

    with patch("os.path.exists", mock_exists):
        show_details({"base_path": "/home/trybe/????"})

        captured = capsys.readouterr()
        assert captured.out == "File '????' does not exist\n"


def test_show_details_analyzing_a_file(capsys):
    context = {
        "base_path": "/home/trybe/Downloads/Trybe_logo.png"
    }

    mock_exists = Mock(return_value=True)
    mock_size = Mock(return_value=3811)
    mock_type = Mock(return_value=False)
    mock_extension = Mock(return_value=("Trybe_logo", ".png"))
    mock_last_modified = Mock(return_value=ts)

    with (
        patch("os.path.exists", mock_exists),
        patch("os.path.getsize", mock_size),
        patch("os.path.isdir", mock_type),
        patch("os.path.splitext", mock_extension),
        patch("os.path.getmtime", mock_last_modified),
    ):
        show_details(context)

    captured = capsys.readouterr()
    assert captured.out == (
        "File name: Trybe_logo.png\n"
        "File size in bytes: 3811\n"
        "File type: file\n"
        "File extension: .png\n"
        "Last modified date: 2023-07-05\n"
    )

def test_show_details_analyzing_a_directory(capsys):
    context = {
        "base_path": "/home/trybe/Downloads"
    }

    mock_exists = Mock(return_value=True)
    mock_size = Mock(return_value=3811)
    mock_type = Mock(return_value=True)
    mock_extension = Mock(return_value=("Downloads", ""))
    mock_last_modified = Mock(return_value=ts)

    with (
        patch("os.path.exists", mock_exists),
        patch("os.path.getsize", mock_size),
        patch("os.path.isdir", mock_type),
        patch("os.path.splitext", mock_extension),
        patch("os.path.getmtime", mock_last_modified),
    ):
        show_details(context)

    captured = capsys.readouterr()
    assert captured.out == (
        "File name: Downloads\n"
        "File size in bytes: 3811\n"
        "File type: directory\n"
        "File extension: [no extension]\n"
        "Last modified date: 2023-07-05\n"
    )