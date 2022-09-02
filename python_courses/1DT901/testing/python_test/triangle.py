"""
Create a Python program triangle.py reading a positive integer N from the
keyboard, and then prints a right-angled triangle. See example below to see what
we mean by right-angled in this case. The program should end with an error message if the input N is a non-positive integer.
"""
"""
Provide a positive integer: 7
      *
     **
    ***
   ****
  *****
 ******
*******
"""
N = -1
while N < 0:
    N = int(input('Enter an positive integer: '))
    
for i in range(N):
    print(' ' * (N - i) + '*' * i)


