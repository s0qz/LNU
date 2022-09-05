'''Problem:
Write a program random_numbers.py that reads a positive integer n from the keyboard and then:
Generates and prints (in a single line) n random numbers in the interval [1,100]
Prints the average value (with two decimals), the smallest number (min), and the largest number (max).
A suitable error message should be presented if the input number n is non-positive.
You should not use a list (or any other data structure) to first store the generated numbers before you compute average, min, and max.
'''
'''Desired output examples:
Enter number of integers to be generated: 10

Generated values: 77 15 13 54 96 73 100 12 98 28 
Average, min, and max are 56.6, 12, and 100
'''




import random
def random_numbers(N):
    for_average = 0
    print(f'Generated values: ', end='')
    lst = [random.randint(1, 100) for i in range(N)]
    for value in lst:
        for_average += value
        print(value, end=' ')
    print(
        f'\nAverage, min, and max are {round(for_average / N)}, {min(lst)}, and {max(lst)}')


N = -1
while N < 1:
    N = int(input('Enter number of integers to be generated: '))

random_numbers(N)
