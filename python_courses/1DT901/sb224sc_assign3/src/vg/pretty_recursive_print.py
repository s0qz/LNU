import os


def pretty_print(dir_path, depth=1):
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_dir():
            print(' ' * depth, entry.name)
            pretty_print(entry.path, depth + 2)


path = os.getcwd()
pretty_print(path)
