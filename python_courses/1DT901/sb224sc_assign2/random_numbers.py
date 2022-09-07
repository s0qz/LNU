# random_numbers.py
#
# Author: Samuel Berg
# Date: 05-Sep-2022
import random


def random_numbers(N):
    for_average = 0
    print('Generated values: ', end='')
    lst = [random.randint(1, 100) for i in range(N)]
    for value in lst:
        for_average += value
        print(value, end=' ')
    avg = round(for_average / N)
    print(
        f'\nAverage, min, and max are {avg}, {min(lst)}, and {max(lst)}')


N = -1
while N < 1:
    N = int(input('Enter number of integers to be generated: '))

random_numbers(N)
