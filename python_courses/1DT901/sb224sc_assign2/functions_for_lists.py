'''Problem:
Create a program called functions_for_lists.py that contains the following for functions:

def random_num_list(n)        #  Generates a list of n integers
def only_odd(lst)             #  Takes a list as input and returns a list with only the odd values
def square(lst)               #  Takes a list as input and creates a new list with all the values squared
def sublist(lst, start, stop) #  Returns a new list with only the values between start and stop in the list

Try to implement these functions as one-liners. The three first are all possible to solve using _list comprehension so try that.
Failing that, you can implement them any way you like.
Also supply example calls to the functions below their definitions. An example execution is shown below:
'''
'''Desired output:
Here is the list: [48, 70, 8, 81, 42]
Odds in it are: [81]
Let's square each number: [2304, 4900, 64, 6561, 1764]
Only the three middle values: [70, 8, 81]
'''

# functions_for_lists.py
#
# Author: Samuel Berg
# Date: 06-Sep-2022




from random import randint
def random_num_list(n):  # Generates a list of n integers
    return [randint(0, 100) for _ in range(n)]


def only_odd(lst):  # Takes a list as input and returns a list with only the odd values
    for i, num in enumerate(lst):
        if num % 2 == 0:
            lst.pop(i)
    return lst


def square(lst):  # Takes a list as input and creates a new list with all the values squared
    for i, num in enumerate(lst):
        lst[i] = num ** 2
    print(f'Let\'s square each number: {lst}')


# Returns a new list with only the values between start and stop in the list
def sublist(lst, start, stop):
    new_lst = []
    for i in range(start, stop):
        new_lst.append(lst[i])
    return new_lst


lst = random_num_list(10)
print(f'Here is the list: {lst}')
print(f'Odds in it are: {only_odd(lst)}')
square(lst)
print(f'Only the three middle values: {sublist(lst, 1,4)}')
