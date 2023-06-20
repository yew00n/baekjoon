import sys
from queue import PriorityQueue

input = sys.stdin.readline
n = int(input())
pq = PriorityQueue()
sum = 0

for i in range(n):
    tempc = list(input())
    for j in range(n):
        temp = 0
        if 'a' <= tempc[j] <= 'z':
            temp = ord(tempc[j]) - ord('a') + 1
        elif 'A' <= tempc[j] <= 'Z':
            temp = ord(tempc[j]) - ord('A') + 27
        sum += temp
        if i != j and temp != 0:
            pq.put((temp, i, j))

parent = [0]*n

for i in range(n):
    parent[i] = i


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


useEdge = 0
result = 0

while pq.qsize() > 0:
    v, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += v
        useEdge += 1

if useEdge == n-1:
    print(sum-result)
else:
    print(-1)
