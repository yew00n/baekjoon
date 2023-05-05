import math
m, n = map(int, input().split())
a = [0]*(n+1)

for i in range(2, n+1):
    a[i] = i

for i in range(2, int(math.sqrt(n)+1)):
    if a[i] == 0:
        continue
    for j in range(i+i, n+1, i):
        a[j] = 0

for i in range(m, n+1):
    if a[i] != 0:
        print(a[i])
