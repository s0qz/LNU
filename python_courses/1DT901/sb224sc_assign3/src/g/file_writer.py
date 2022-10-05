import os


def writing(path, name, content):
    file = open(path + '/' + name, 'a')
    file.write(content + '\n')
    file.close()
    msg = input('> ')
    if msg == 'stop':
        exit()
    else:
        writing(path, file_name, msg)


path = os.getcwd()
path = path + '/out'

file_name = input('Name of the file: ')
file = open(path + '/' + file_name, 'x')
file.close()
print('Enter the content and end with "stop":')
msg = input('> ')
writing(path, file_name, msg)
