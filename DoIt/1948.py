import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

time = [0] * (N+1)
in_degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
bgraph = [[] for _ in range(N+1)]
cnt = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    bgraph[b].append(a)
    in_degree[b] += 1

src, dst = map(int, input().split())

q = deque([])
q.append(src)

while q:
    now = q.popleft()
    for i in graph[now]:
        in_degree[i[1]] -= 1
        if time[i[1]] < time[now] + i[0]:
            time[i[1]] = time[now] + i[0]
            cnt[i[1]] = [now]
        elif time[i[1]] == time[now] + i[0]:
            cnt[i[1]].append(now)

        if in_degree[i[1]] == 0:
            q.append(i[1])

q = deque([dst])
route = set()
while q:
    now = q.popleft()
    for x in cnt[now]:
        if (now, x) not in route:
            route.add((now, x))
            q.append(x)

print(time[dst])
print(len(route))
