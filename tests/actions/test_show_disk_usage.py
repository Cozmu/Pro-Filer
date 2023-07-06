from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from unittest.mock import Mock, patch
import os

def test_show_disk_usage_with_content(capsys, tmp_path):
    output_path_one = tmp_path / 'app.py'
    output_path_one.touch()
    output_path_one.write_text('string muito grande')
    output_path_two = tmp_path / '__init__.py'
    output_path_two.touch()
    output_path_two.write_text('string')

    context = {
        "all_files": [
            str(output_path_one),
            str(output_path_two),
        ]
    }
    mock__get_printable_file_path_one = Mock(return_value=str(output_path_one))
    mock__get_printable_file_path_two = Mock(return_value=str(output_path_two))

    with ( 
        patch("pro_filer.cli_helpers._get_printable_file_path", mock__get_printable_file_path_one),
        patch("pro_filer.cli_helpers._get_printable_file_path", mock__get_printable_file_path_two)
    ):
        show_disk_usage(context)


    captured = capsys.readouterr()
    assert captured.out == (
        "'/tmp/pytest-of-usuario/pyte...w_disk_usage_with_cont0/app.py':        19 (76%)\n"
        "'/tmp/pytest-of-usuario/pyte...k_usage_with_cont0/__init__.py':        6 (24%)\n"
        "Total size: 25\n"
    )


def test_show_disk_usage_no_files(capsys):
    context = { "all_files": [] }
    show_disk_usage(context)
    result = capsys.readouterr()
    assert result.out == "Total size: 0\n"