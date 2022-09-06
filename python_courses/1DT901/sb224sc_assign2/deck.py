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
from random import randint
values = list(range(2, 15))
colors = ['of Hearts', 'of Diamonds', 'of Spades', 'of Clubs']

face_cards = {
    11: 'Jack',
    12: 'Queen',
    13: 'King',
    14: 'Ace'
}


class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color


def generate_deck(value, color):
    deck = []
    for value in values:
        for color in colors:
            if value in face_cards:
                card_value = face_cards[value]
                deck.append(Card(card_value, color))
            else:
                deck.append(Card(value, color))
    return deck


deck = generate_deck(values, colors)

for card in deck:
    print(card.value, card.color)


def shuffle(deck):
    for i in range(0, 52):
        r = randint(0, i)
        deck[i], deck[r] = deck[r], deck[i]


deck = shuffle(deck)
print('My hand: ')
for _ in range(0, 5):
    r = randint(0, 52)
    print(f'{deck[r]}')
    deck.pop(r)
