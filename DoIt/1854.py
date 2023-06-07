import sys
import heapq
input = sys.stdin.readline
n, m, k = map(int, input().split())
w = [[] for _ in range(n+1)]
distance = [[sys.maxsize]*k for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    w[a].append((b, c))

pg = [(0, 1)]
distance[1][0] = 0

while pq:
    cost, node = heapq.heappop(pq)
    for nNode, nCost in w[node]:
        sCost = cost + nCost
        if distance[nNode][k-1] > sCost:
            distance[nNode][k-1] = sCost
            distance[nNode].sort()
            heapq.heappush(pq, [sCost, nNode])

for i in range(1, n+1):
    if distance[i][k-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][k-1])
