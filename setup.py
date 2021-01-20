from cx_Freeze import setup, Executable

base = None

executables = [Executable("game.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "playablegame",
    options = options,
    version = "1.0",
    description = 'The official playable game file.',
    executables = executables
)