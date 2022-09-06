'''Problem:
A magic 8-ball will answer question you ask it in a random way (yes, they do not work for real...).
Create a program called eightball.py that has a list of strings of possible answers.
The program should ask the user to ask a question and it will randomly pick one of the strings in the list as an answer.
The program will stop when the user enters the string stop, and it will stop at once not giving any more answers. 
'''
'''Desired output:
Ask the magic 8-ball your question: Will I win the lottery?
The magic 8-ball says: Ask again later
Ask the magic 8-ball your question: Okay, will I win the lottery?
The magic 8-ball says: As I see it, yes
Ask the magic 8-ball your question: Will I win a lot of money?
The magic 8-ball says: Concentrate and ask again
Ask the magic 8-ball your question: Okay... Will I get rich?
The magic 8-ball says: As I see it, yes
Ask the magic 8-ball your question: Great! Will I be a millionaire?
The magic 8-ball says: Better not tell you now
Ask the magic 8-ball your question: Why? Please tell me if I will...
The magic 8-ball says: Very doubtful
Ask the magic 8-ball your question: stop
'''
from random import randint
magic_ball = ['Ask again later',
              'As I see it, yes', 'Concentrate and ask again', 'Better not tell you now', 'Very doubtful']
i = 'None'

while i != 'stop':
    i = input('Ask the magic 8-ball your question: ').lower()
    if i == 'stop':
        exit()
    else:
        print(f'The magic 8-ball says: {magic_ball[randint(0, 4)]}')
