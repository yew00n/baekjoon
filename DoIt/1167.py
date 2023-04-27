from collections import deque

n = int(input())
a = [[] for _ in range(n+1)]

for _ in range(n):
    data = list(map(int, input().split()))
    index = 0
    s = data[index]
    index += 1
    while True:
        e = data[index]
        if e == -1:
            break
        v = data[index+1]
        a[s].append((e, v))
        index += 2

distance = [0] * (n+1)
visited = [False] * (n+1)


def BFS(v):
    queue = deque()
    queue.append(v)
    while queue:
        node = queue.popleft()
        for i in a[node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[node] + i[1]
