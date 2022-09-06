'''Problem:
Write a program called list_info.py that creates a list with 100 elements that are random values between 1 and 10000.
The program should then print out the largest, smallest, average (rounded to two decimals) and second largest value in the list.
See below for an example execution:
'''
'''Desired output:
Largest value in list: 9973
Smallest value in list: 22
Average value in list: 4677.61
Second largest value in list: 9941
'''
from random import randint
lst = [randint(1, 10000) for i in range(100)]
num = 0

print(f'Largest value in list: {max(lst)}')
print(f'Smallest value in list: {min(lst)}')

for i in lst:
    num += i
print(f'Average value in list: {round(num/len(lst), 2)}')

lst.sort()
print(f'Second largest value in list: {lst[-2]}')
