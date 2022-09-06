'''Problem:
A sentence can consist of a pronoun followed by a verb and a noun.
If the sentence is in future tense, a sentence could be "I will paint a house",
where "I" is the pronoun, "will paint" is the verb and "a house" is the noun.
Create a program called sentence_builder.py that has three functions called pronoun(),
verb() and noun() respectively. Each function should randomly pick one of five of each kind
(meaning that the function pronoun() should select one of "I", "You", "It", "We", "They").
After the function definitions you should have an iteration which creates ten random sentences by calling the three functions.
'''
'''Desired output:
It will see a house
They will eat a house
You will pull a car
I will see a house
I will touch a computer
You will eat a tree
You will touch a house
I will touch a car
I will see a tree
'''

# sentence_builder.py
#
# Author: Samuel Berg
# Date: 05-Sep-2022

from random import randint
PRONOUN = ['It', 'They', 'You', 'I', 'We']
VERB = ['will see', 'will eat', 'will pull', 'will touch', 'will paint']
NOUN = ['a house', 'a car', 'a computer', 'a tree', 'an elephant']


def pronoun() -> str:
    var = randint(0, 4)
    return PRONOUN[var]


def verb() -> str:
    var = randint(0, 4)
    return VERB[var]


def noun() -> str:
    var = randint(0, 4)
    return NOUN[var]


for _ in range(10):
    print(f'{pronoun()} {verb()} {noun()}')
