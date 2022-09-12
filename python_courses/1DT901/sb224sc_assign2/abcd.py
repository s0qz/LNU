# abcd.py
#
# Author: Samuel Berg
# Date: 12-Sep-2022

def get_number(a, b, c, d):
    abcd = int(str(a) + str(b) + str(c) + str(d))
    dcba = int(str(d) + str(c) + str(b) + str(a))
    if (4 * abcd) == dcba:
        print(abcd)


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for a in numbers:
    if a != 0:
        for b in numbers:
            for c in numbers:
                for d in numbers:
                    if d != 0:
                        get_number(a, b, c, d)
