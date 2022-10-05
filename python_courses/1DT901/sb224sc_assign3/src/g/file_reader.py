import os


def reading(path, name):
    with open(path + '/' + name, 'r') as file:
        temp = file.readlines()
        print(f'Lines in file: {len(temp)}')
        print('Content of file:')
        for line in temp:
            line = line.strip('\n')
            print(line)


path = os.getcwd()
path = path + '/out'

file_name = input('What is the name of the file to read? ')
reading(path, file_name)
