import math
min, max = map(int, input().split())
A = [0]*(1000001)

for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A+1)))):
    if A[i] == 0:
        continue
    for j in range(i+1, len(A), i):  # 배수를 지움
        A[j] = 0

count = 0

for i in range(2, 10000001):
    if A[i] != 0:  # 소수
        temp = A[i]
        while A[i] <= max/temp:
            if A[i] >= min/temp:
                count += 1
            temp = temp * A[i]

print(count)
