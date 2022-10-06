# Character.py
#
# Author: Samuel Berg
# Date: 03-Oct-2022

import os


def print_sub(dir_path):
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_dir():
            print(entry.name)
            print_sub(entry.path)


path = os.getcwd()
print_sub(path)
