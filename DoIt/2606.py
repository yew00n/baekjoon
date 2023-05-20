from collections import deque

n = int(input())
v = int(input())
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)

for i in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
visited[1] = 1  # 방문 표시

Q = deque([1])
while Q:
    c = Q.popleft()
    for n in graph[c]:
        if visited[n] == 0:
            Q.append(n)
            visited[n] = 1
print(sum(visited)-1)
