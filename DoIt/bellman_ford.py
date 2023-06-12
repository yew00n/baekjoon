graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}


def bellman_ford(graph, start):
    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node] = float('inf')
        predecessor[node] = None
    distance[start] = 0

    # 정점 개수(v-1)만큼 반복
    for i in range(len(graph)-1):
        for node in graph:
            for neighbor in graph[node]:
                if distance[neighbor] > distance[node] + graph[node][neighbor]:
                    # 최단거리 갱신
                    distance[neighbor] = distance[node] + graph[node][neighbor]
                    predecessor[neighbor] = node

    # 음수 사이클 판별
    for node in graph:
        for neighbor in graph[node]:
            if distance[neighbor] > distance[node] + graph[node][neighbor]:
                return -1

    return distance, predecessor


print(bellman_ford(graph, 'A'))
