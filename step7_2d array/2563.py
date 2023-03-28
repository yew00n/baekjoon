import sys

paper = [[0]*101 for _ in range(101)]
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    for row in range(x, x+10):
        for col in range(y, y+10):
            paper[row][col] = 1

result = 0
for i in paper:
    result += i.count(1)

print(result)
