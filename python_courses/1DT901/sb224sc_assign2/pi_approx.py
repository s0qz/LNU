# pi_approx.py
#
# Author: Samuel Berg
# Date: 12-Sep-2022

from math import pi
from random import uniform


def pi_approx(N):
    for _ in range(N):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if (in_unit_circle(x, y)):
            points.append([x, y])
    approx = SQUARE_AREA * (len(points) / N)
    print(f'PI is approximately: {approx}')
    print(f'Difference between actual pi and approximated: {abs(pi - approx)}')


def in_unit_circle(x, y):
    if pow(x, 2) + pow(y, 2) <= RADIUS:
        return True
    else:
        return False


RADIUS = 1
SQUARE_AREA = 4
points = []

pi_approx(100)
pi_approx(10000)
pi_approx(1000000)
