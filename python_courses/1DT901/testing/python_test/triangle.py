N = -1
while N < 0:
    N = int(input('Enter an positive integer: '))

for i in range(N):
    print(' ' * (N - i) + '*' * i)
