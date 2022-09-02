'''Problem:
Create a program called print_primes.py that asks for a number of prime numbers to print.
The program should then print them ten at a line and then continue on the next line.
'''
'''Desired output examples:
How many primes? 50
2 3 5 7 11 13 17 19 23 29
31 37 41 43 47 53 59 61 67 71
73 79 83 89 97 101 103 107 109 113
127 131 137 139 149 151 157 163 167 173
179 181 191 193 197 199 211 223 227 229
'''

# print_primes.py
# 
# Author: Samuel Berg
# Date: 01-Sep-2022

# Computes whether or not the given number is prime
def check_if_prime(N) -> bool:
    for i in range(2, N):
        if(N % i == 0):
            return False
    return True

# Creation "variables"
primes = []
N = -1

# Reads input
amount_of_primes = int(input('How many primes? '))


while(len(primes) < amount_of_primes):
    if(check_if_prime(N) == True and N > 1):
        primes.append(N)
        N += 1
    else: 
        N += 1
        
for i in range(len(primes)):
    if(i == 0 or (i % 10) != 0):
        print(primes[i], end=' ')
    else:
        print(f'\n{primes[i]}', end=' ')


