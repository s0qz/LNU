'''Problem: 
Inside file distance.py, create a function distance(x1,y1,x2,y2) which computes the
distance between two points x1,y1 and x2,y2 using the formula

distance = Sqrt( (x1-x2)^2 + (y1-y2)^2 )
Sqrt() means "the square root of" and ^ means "raised to".

Also, add program code so that a user can provide the point coordinates and get the distance.
The answer should be presented with three decimal digits as in the example below:
'''
'''Desired output:
Enter x1: 1
Enter y1: 1
Enter x2: 5
Enter y2: 6

The distance between (1.0,1.0) and (5.0,6.0) is 6.403
'''

# distance.py
#
# Author: Samuel Berg
# Date: 06-Sep-2022

from math import sqrt
def distance(x1, y1, x2, y2):
    return round(sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)), 3)


x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))

print(
    f'The distance between ({x1},{y1}) and ({x2},{y2}) is {distance(x1, y1, x2, y2)}')
