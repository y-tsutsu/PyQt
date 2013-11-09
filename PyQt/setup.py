import sys
from cx_Freeze import setup, Executable
 
includes = ["PyQt5.QtCore","PyQt5.QtGui","PyQt5.QtWidgets","re",]
 
base = None
if sys.platform == "win32":
    base = "Win32GUI"
 
setup(  name = "ramen_timer",
        version = "1.0",
        options = {"build_exe": {"includes": includes}},
        executables = [Executable("ramen_timer.pyw", base=base)])
		