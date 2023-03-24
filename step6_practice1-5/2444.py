n = int(input())

for row in range(1, n):
    print(" "*(n-row) + "*"*(row*2-1))
for row in range(n, 0, -1):
    print(" "*(n-row) + "*"*(row*2-1))
