import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "ramen_timer",
        version = "1.0",
        options = {"build_exe": {
            "includes": "atexit",
            "include_files": [(r"c:\python34\lib\site-packages\PyQt5\libEGL.dll", "")]
        }},
        executables = [Executable("ramen_timer.pyw", base=base)])
