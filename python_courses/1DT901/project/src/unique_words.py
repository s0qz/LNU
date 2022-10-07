# unique_words.py
#
# Author: Samuel Berg
# Date: XX-Oct-2022         Change date when done

# import BstMap
# import HashSet
import os


def open_news():
    with open(swe_news_txt, 'r') as file:
        lst = file.readlines()
    return lst


def open_brian():
    with open(life_of_brian_txt, 'r') as file:
        lst = file.readlines()
    return lst


def count_unique_words(lst):
    myset = set()
    for i in range(len(lst)):
        myset.add(lst[i])
    new_lst = list(myset)
    return len(new_lst)


def get_top10(lst):
    top10 = {}
    for word in lst:
        striped_word = word.strip('\n')
        if striped_word not in top10:
            top10[striped_word] = 0
        top10[striped_word] += 1
    '''
    iterate over top10 and remove all but the 10 most frequent words
    '''
    return top10


# Main code
path = os.getcwd()
path = path + ('/data/')

life_of_brian_txt = f'{path}brian_13159_words.txt'
swe_news_txt = f'{path}swe_news_14337973_words.txt'

life_of_brian = open_brian()
swe_news = open_news()

unique_brian = count_unique_words(life_of_brian)
unique_news = count_unique_words(swe_news)

top10_brian = get_top10(life_of_brian)
top10_news = get_top10(swe_news)
print(top10_brian)
