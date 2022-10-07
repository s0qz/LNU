# unique_words.py
#
# Author: Samuel Berg
# Date: 07-Oct-2022

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
    all_count = {}
    for word in lst:
        striped_word = word.strip('\n')
        if striped_word not in all_count:
            all_count[striped_word] = 0
        all_count[striped_word] += 1
    '''
    iterate over all_count and remove the 10 most frequent words
    after adding them to the top10 dict
    '''
    for _ in range(10):
        highestfreq_val = 0
        highestfreq_key = ''
        for key in all_count:
            if all_count[key] > highestfreq_val:
                highestfreq_key = key
                highestfreq_val = all_count[key]
        if highestfreq_key not in top10:
            top10[highestfreq_key] = 0
        top10[highestfreq_key] += highestfreq_val
        all_count.update({highestfreq_key: 0})
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

print(f'Amount of unique words in life of brian: {unique_brian}')
print('\nTop 10 most occurring words in life of brian:')
for key in top10_brian:
    print(f'"{key}"\t{top10_brian[key]}')

print(f'\nAmount of unique words in swe news: {unique_news}')
print('\nTop 10 most occurring words in swe news:')
for key in top10_news:
    print(f'"{key}"\t{top10_news[key]}')
