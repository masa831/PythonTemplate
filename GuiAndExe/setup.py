import sys
from cx_Freeze import setup, Executable

# https://zenn.dev/musashi26629/articles/c8aae7d3f6f863

base = None
package = []
include = []

build_exe_options = {
    "packages": package,
    "includes": include
}

exe = Executable(script = "testTk.py", base=base, icon="./icon/penguin.ico")

if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="testApp_cx",
    version="0.1",
    description="test application",
    options={"build_exe": build_exe_options},
    executables=[exe],
)

# comand
# python setup.py build --iconfile=xx.ico
