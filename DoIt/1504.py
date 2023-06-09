import sys
from queue import PriorityQueue
input = sys.stdin.readline
n, m = map(int, input().split())
adjacent = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    adjacent[a].append((b, w))
    adjacent[b].append((a, w))

a, b = map(int, input().split())
possible = True


def dijkstra(start, end):
    global possible
    dist = [sys.maxsize] * (n+1)
    dist[start] = 0
    visited = [False] * (n+1)
    queue = PriorityQueue()
    queue.put((0, start))
    while queue.qsize() != 0:
        node = queue.get()
        if visited[node[1]]:
            continue
        visited[node[1]] = True
        for i in adjacent[node[1]]:
            distance = node[0] + i[1]
            if distance < dist[i[0]]:
                dist[i[0]] = distance
                queue.put((distance, i[0]))
    if dist[end] == sys.maxsize:
        possible = False
        return 0
    return dist[end]


result_1 = dijkstra(1, a) + dijkstra(a, b) + dijkstra(b, n)
result_2 = dijkstra(1, b) + dijkstra(b, a) + dijkstra(a, n)
if possible:
    print(min(result_1, result_2))
else:
    print("-1")
