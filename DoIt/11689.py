import math
n = int(input())
result = n

for p in range(2, int(math.sqrt(n))+1):
    if n % p == 0:
        result -= result / p
        while n % p == 0:
            n /= p

if n > 1:
    result -= result / n

print(int(result))
