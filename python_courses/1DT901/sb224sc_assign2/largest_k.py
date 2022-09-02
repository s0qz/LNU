'''Problem:
Write a program largest_k.py which for any given positive integer n (read from the keyboard) computes the largest integer k such that 0 + 2 + 4 + 6 + 8 + ... + k < n.
Notice: The program should be terminated with a suitable error message if a non-positive n is provided.
'''
'''Desired output examples:
Enter a positive integer: 25
8 is the largest k such that 0+2+4+6+...+k < 25
'''

# largest_k.py
# 
# Author: Samuel Berg
# Date: 01-Sep-2022

# Computes the largest integer k
def largest_k(N):
    iterator = 0
    sum = 0
    while((sum + iterator) < N):
        sum += iterator
        iterator += 2
    iterator -= 2
    return iterator

# Reads input
N = int(input('Enter a positive integer: '))

# Calls func largest_k
k = largest_k(N)

# Prints result
print(f'{k} is the largest k such that 0+2+4+6+...+k < {N}')

