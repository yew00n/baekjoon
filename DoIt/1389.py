import sys
n, m = map(int, input().split())
distance = [[sys.maxsize for j in range(n+1)] for i in range(n+1)]

for i in range(1, n+1):
    distance[i][i] = 0

for i in range(m):
    s, e = map(int, input().split())
    distance[s][e] = 1
    distance[e][s] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

Min = sys.maxsize
Answer = -1

for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        temp += distance[i][j]
    if Min > temp:
        Min = temp
        Answer = i

print(Answer)
