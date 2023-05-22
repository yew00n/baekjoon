from queue import PriorityQueue
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
distance = [sys.maxsize]*(V+1)  # 노드 개수보다 하나 더
visited = [False] * (V+1)
myList = [[] for _ in range(V+1)]  # 인접리스트. 이중 리스트
q = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split())
    myList[u].append(v, w)

q.put((0, K))  # 거리의 값을 기준으로 최소값인 것을 자동으로 선택하도록 하기 위함
distance[K] = 0

while q.qsize() > 0:
    current = q.get()
    current_v = current[1]  # 목표 가중치를 가져오기 위함
    if visited[current_v]:
        continue
    visited[current_v] = True
    for temp in myList[current_v]:
        next = temp[0]
        value = temp[1]  # 가중치
        if distance[next] > distance[current_v] + value:
            distance[next] = distance[current_v] + value
            q.put((distance[next], next))

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")
