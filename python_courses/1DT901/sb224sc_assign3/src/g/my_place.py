import os


def count_directories(dir_path):  # Returns the number of directories
    folders = 0
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_dir():
            folders += 1
    return folders


def count_files(dir_path):  # Returns the number of files
    files = 0
    for _, _, filenames in os.walk(dir_path):
        files += len(filenames)
        return files


path = os.getcwd()

print(f'I am right now at: {path}')
print(f'Below me I have {count_directories(path)} directories/folders')
print(f'This directory contains {count_files(path)} files')
