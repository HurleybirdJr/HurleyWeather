from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

build_exe_options = {"include_files": ['open.wav'], "packages": ["os","queue","os","idna","geopy","sys","time","datetime","requests","winsound","colorama"], "excludes": ["tkinter"]}

setup(
    name="DarkSky",
    version="1.0",
    description="Weather Forecast Powered By DarkSky API",
    options = {"build_exe": build_exe_options},
    executables = [Executable(script="DarkSky.py", icon="icon.ico", base="Console")]
    )
