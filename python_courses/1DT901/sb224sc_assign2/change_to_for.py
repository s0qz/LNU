'''Problem:
Write a program that you call change_to_for.py where you convert the following program that is using a while iteration into a program that uses for instead.
The output must be the same for both programs.
'''
'''Convert so it uses for loops:
count = 0
sum = 0

while count < 100:
    sum = sum + count
    count = count + 1

print(count)
'''

# change_to_for.py
# 
# Author: Samuel Berg
# Date: 01-Sep-2022

count = 0
sum = 0

while count < 100:
    sum = sum + count
    count = count + 1

print(count)    # Is it supposed to print sum? Otherwise sum is useless

#########################################################################

count = 0
sum = 0

for i in range(100):
    sum += count
    count += 1

print(count)    # Is it supposed to print sum? Otherwise sum is useless
