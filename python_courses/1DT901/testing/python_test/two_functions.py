""" Problem
• A function positive_int(float_lst) that returns a new list with
all the positive numbers in the float list float_lst correctly rounded off
to integers. For example, the input [1.3, 2.67, -2.25, 4.88] the
function should return [1, 3, 5].
• A function largest_K(N) which for any given positive integer N computes and returns the largest integer K such that 1+ 3+ 5+ 7+...+K < N(40).
For example, input N = 40 should give K = 11.
Also, add program code that demonstrates how the two functions can be used.
"""
def positive_int(float_lst):
    int_lst = []
    for i in float_lst:
        if(i > 0):
            int_lst.append(round(i))
    
    return int_lst

def largest_K(N):
    iterator = 1
    sum = 0
    while((sum + iterator) < N):
        sum += iterator
        iterator += 2
    return iterator

float_lst = [1.3, 2.67, -2.25, 4.88]
print(positive_int(float_lst))
print(largest_K(40))

