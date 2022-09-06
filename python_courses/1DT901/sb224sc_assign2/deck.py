'''Problem:
Normal playing cards consist of 52 cards with suits (Hearts, Spades, Clubs and Diamonds) and a value (1 to 10 followed by Jack, Queen, King and Ace).
Create a program called deck.py that creates such a deck (with all 52 cards) and then shuffles it.
The program should then print out the five top cards as "My hand". See below for an execution:
'''
'''Desired output:
My hand:
3 of Hearts
10 of Clubs
6 of Spaces
5 of Spaces
Ace of Diamonds
'''

# deck.py
#
# Author: Samuel Berg
# Date: 06-Sep-2022

from random import randint, shuffle
values = ['2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ',
          '9 ', '10 ', 'Jack ', 'Queen ', 'King ', 'Ace ']
colors = ['of Hearts', 'of Spades', 'of Diamonds', 'of Clubs']
face_cards = ['Jack', 'Queen', 'King', 'Ace']

deck = []

for value in values:
    for color in colors:
        tmp = value + color
        deck.append(tmp)

shuffle(deck)

print('My hand:')
for i in range(5):
    print(f'{deck[i]}')
