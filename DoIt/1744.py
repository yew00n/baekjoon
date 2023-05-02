import sys
input = sys.stdin.readline

n = int(input())
pos = []
neg = []
max_sum = 0

for _ in range(n):
    n = int(input())

    if n > 1:
        pos.append(n)
    elif n == 1:
        max_sum += 1
    else:
        neg.append(n)

pos.sort(reverse=True)
neg.sort()

if len(pos) % 2 == 0:
    for i in range(0, len(pos), 2):
        max_sum += pos[i] * pos[i+1]
else:
    for i in range(0, len(pos)-1, 2):
        max_sum += pos[i] * pos[i+1]
    max_sum += pos[len(pos)-1]

if len(neg) % 2 == 0:
    for i in range(0, len(neg), 2):
        max_sum += neg[i] * neg[i+1]
else:
    for i in range(0, len(neg)-1, 2):
        max_sum += neg[i] * neg[i+1]
    max_sum += neg[len(neg)-1]

print(max_sum)
