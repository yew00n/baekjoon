import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
isEven = True


def DFS(node):
    global isEven
    visited[node] = True
    for i in a[node]:
        if not visited[i]:
            check[i] = (check[node]+1) % 2
            DFS(i)
        elif check[node] == check[i]:
            isEven = False


for _ in range(n):
    v, e = map(int, input().split())
    a = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    check = [0]*(v+1)
    isEven = True

for _ in range(e):
    start, end = map(int, input().split())
    a[start].append(end)
    a[end].append(start)

for i in range(1, v+1):
    if isEven:
        DFS(i)
    else:
        break

    if isEven:
        print("YES")
    else:
        print("NO")
