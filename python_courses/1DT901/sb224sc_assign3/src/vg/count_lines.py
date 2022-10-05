import os


def count_py_lines(dir_path):
    count = 0
    for subdir, _, files in os.walk(dir_path):
        for file in files:
            if file.startswith('.'):
                pass
            else:
                if file.endswith('.py'):
                    with open(f'{subdir}/{file}', 'r', encoding='utf-8') as f:
                        temp = f.readlines()
                        for line in temp:
                            if line == '\n':
                                temp.remove(line)
                        count += len(temp)
    return count


os.chdir('..')
path = (os.getcwd())

print(count_py_lines(path))
