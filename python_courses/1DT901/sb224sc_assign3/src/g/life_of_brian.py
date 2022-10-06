# Character.py
#
# Author: Samuel Berg
# Date: 06-Oct-2022

import os


def get_words(path, file_name):
    temp = []
    allowed_words = []
    with open(path + file_name, 'r', encoding='utf-8') as f:
        original = f.readlines()
        for line in original:
            line = line.lower()
            line = line.replace('-', '')
            line = line.replace("'", '')
            line = line.replace('.', ' ')
            line = line.replace(',', ' ')
            line = line.replace('!', ' ')
            line = line.replace('?', ' ')
            line = line.replace(":", ' ')
            line = line.strip('\n')
            temp.append(line.split(' '))

        for line in temp:
            for word in line:
                if len(word.replace(' ', '')) == 1:
                    if word == 'a' or word == 'i':
                        allowed_words.append(word)
                elif word.isalpha() or word.isspace():
                    allowed_words.append(word)
        return allowed_words


def save_words(path, name, words):
    with open(path + name, 'a', encoding='utf-8') as f:
        for word in words:
            f.write(word + '\n')


path = os.getcwd()
input_file = '/data/life_of_brian.txt'

words = get_words(path, input_file)

output_file = f'/out/brian_{len(words)}_words.txt'

save_words(path, output_file, words)
print('Saved', len(words), 'words in the file', path + output_file)
