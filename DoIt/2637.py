import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
V = int(input())
E = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
needs = [[0]*(N+1) for _ in range(N+1)]

for i in range(V):
    a, b, c = map(int, input().split())
    E[b].append([a, c])
    indegree[a] += 1

q = deque()
basic_parts = []
for i in range(1, N+1):
    if indegree[i] == 0:
        basic_parts.append(i)
        q.append(i)

while q:
    now = q.popleft()
    for object, n in E[now]:
        if now in basic_parts:
            needs[object][now] += n
        else:
            for i in range(1, N+1):
                needs[object][i] += needs[now][i]*n
        indegree[object] -= 1
        if indegree[object] == 0:
            q.append(object)

for i in range(N+1):
    if needs[N][i] > 0:
        print(i, needs[N][i])
