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
