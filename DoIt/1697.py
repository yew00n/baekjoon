import sys
from collections import deque


def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return array[v]
        for v2 in (v-1, v+1, 2*v):
            if 0 <= v2 < 100001 and not array[v2]:
                array[v2] = array[v] + 1
                q.append(v2)


n, k = map(int, sys.stdin.readline().split())
array = [0] * 100001
print(bfs(n))
