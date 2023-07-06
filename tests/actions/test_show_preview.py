from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_without_content(capsys):
    show_preview({"all_files": [], "all_dirs": []})
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"

def test_show_preview_with_content(capsys):
    context = {
        "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
        "all_dirs": ["src", "src/utils"]
    }
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == (
        "Found 3 files and 2 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']\n"
        "First 5 directories: ['src', 'src/utils']\n"
        )


def  test_show_preview_with_full_content(capsys):
    context = {
        "all_files": [
            "src/__init__.py", "src/app.py", "src/utils/__init__.py", "src/arquivo.py", "src/index.py", "src/util.py"
            ],
        "all_dirs": [
            "src", "src/utils", "src/services", "src/seeders", "src/middlewares", "src/controlllers"
            ]
    }
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == (
        "Found 6 files and 6 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', "
        "'src/utils/__init__.py', 'src/arquivo.py', 'src/index.py']\n"
        "First 5 directories: ['src', 'src/utils', 'src/services', "
        "'src/seeders', 'src/middlewares']\n"
    )