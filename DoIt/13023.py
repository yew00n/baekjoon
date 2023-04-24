import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())
arrived = False
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)


def DFS(now, depth):
    global arrived
    if depth == 5:
        arrived = True
        return
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i, depth + 1)
    visited[now] = False


for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(n):
    DFS(i, 1)
    if arrived:
        break

if arrived:
    print(1)
else:
    print(0)
