"""
Open file using Windows file association
but first try to see if there's a better file
available in better format (ie: MP4 vs AVI)
"""

# pylint: disable=line-too-long

import argparse
import ctypes
import os
import sys
import re

BETTER_EXT = {
    "avi": "mp4",
    "bmp": "jpeg",
}

class Win32ArgumentParser(argparse.ArgumentParser):
    """ Argument parser with Windows error message box """

    def error(self, message):
        """ Show error in windows box """
        ctypes.windll.user32.MessageBoxW(0, message, "Argument parser error", 0)
        sys.exit(1)

def cli_args():
    """ Parse command line arguments """

    parser = Win32ArgumentParser(description=__doc__.strip())
    parser.add_argument("filepath", type=str, help="filepath to open", metavar="/path/to/file.avi")
    config = parser.parse_args()
    return config

def open_file(filepath):
    """
    Open given path with associated application
    or better file if available or show and error box
    """

    file_ext = filepath.split(".")[-1]
    if file_ext.lower() in BETTER_EXT:

        better_filepath = re.sub(r"\.%s$" % file_ext, ".%s" % BETTER_EXT[file_ext.lower()], filepath)

        if os.path.isfile(better_filepath) and os.access(better_filepath, os.R_OK):
            # Will annoy user but useful for debugging
            #ctypes.windll.user32.MessageBoxW(0, "Opening better file %s" % better_filepath, "Better file found", 0)
            os.startfile(better_filepath)
            return

    if os.path.isfile(filepath) and os.access(filepath, os.R_OK):
        os.startfile(filepath)
    else:
        message = "File %s does not exist" % filepath
        ctypes.windll.user32.MessageBoxW(0, message, message, 0)
        sys.exit(1)

if __name__ == "__main__":

    CONFIG = cli_args()
    open_file(CONFIG.filepath)
