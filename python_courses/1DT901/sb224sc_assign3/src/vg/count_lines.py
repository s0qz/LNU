import os


def count_py_lines(dir_path):
    count = 0
    for subdir, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.py'):
                f = open(f'{subdir}/{file}', 'r')
                temp = f.readlines()
                for line in temp:
                    if line == '\n':
                        temp.remove(line)
                count += len(temp)
                f.close()
    return count


os.getcwd()
os.chdir('../../../')
print(count_py_lines(os.getcwd()))
