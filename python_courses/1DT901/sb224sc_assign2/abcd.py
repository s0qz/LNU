'''Problem:
There are four different digits A, B, C, and D such that the number DCBA is equal to 4 times the number ABCD.
What are the four digits? Note: to make ABCD and DCBA a proper four digit integer, neither A nor D can be zero.
The name of the program computing A, B, C, and D should be named abcd.py.
Hint: Use a quadruple nested loop and a function get_number(a, b, c, d) that converts digits a, b, c, d into a four digit integer abcd.
'''
def get_number(a, b, c, d):
    tmp = f'{a}{b}{c}{d}'
    return int(tmp)
