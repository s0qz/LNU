def positive_int(float_lst):
    int_lst = []
    for i in float_lst:
        if (i > 0):
            int_lst.append(round(i))

    return int_lst


def largest_K(N):
    iterator = 1
    sum = 0
    while ((sum + iterator) < N):
        sum += iterator
        iterator += 2
    return sum


float_lst = [1.3, 2.67, -2.25, 4.88]
print(positive_int(float_lst))
print(largest_K(3))
