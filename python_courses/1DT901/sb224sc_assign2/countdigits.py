'''Problem:
Counting Digits (VG)
Write a program countdigits.py, which for any given positive number n (read from the keyboard) prints the number of zeros, odd digits, and even digits of the integer.
In this case we consider zeros to be neither odd nor even.
'''
'''Desired output examples:
Enter a large positive integer: 6789500

Zeros: 2
Odd: 3
Even: 2
'''

# countdigits.py
#
# Author: Samuel Berg
# Date: 05-Sep-2022

def count_digits(N):
    zero = 0
    even = 0
    odd = 0
    for i in N:
        i = int(i)
        if i == 0:
            zero += 1
        elif i % 2 == 0:
            even += 1
        else:
            odd += 1

    print(f'Zeros: {zero}')
    print(f'Odd: {odd}')
    print(f'Even: {even}')


N = input('Enter a large positive integer: ')

count_digits(N)
