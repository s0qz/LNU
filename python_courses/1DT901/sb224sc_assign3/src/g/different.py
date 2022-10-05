from random import randint


def different(lst):
    myset = set()
    for i in range(len(lst)):
        myset.add(lst[i])
    new_lst = list(myset)
    return new_lst


lst = list(randint(0, 200) for i in range(0, 100))

print(f'Different integers:\n{different(lst)}')
