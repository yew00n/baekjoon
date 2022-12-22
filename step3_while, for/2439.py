row = 1
N = int(input())

while row <= N:
    print(' '*(N-row),end='')
    print('*'*row)
    row += 1