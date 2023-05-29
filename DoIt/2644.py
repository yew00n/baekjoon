N = int(input())
S, E = map(int, input().split())
M = int(input())
adj = [[] for _ in range(N+1)]


def bfs(s, e):
    q = []
    visited = [0]*(N+1)

    q.append(s)
    visited[s] = 1  # 초기값 설정

    while q:
        c = q.pop(0)  # current
        if c == e:
            return visited[e]-1  # 시작부터 1을 넣었기 때문

        for i in adj[c]:
            # c와 연결되고, 미방문된 경우이면 방문하기
            if visited[i] == 0:
                visited[i] = visited[i]+1  # 1씩 늘려서 촌수 계산
                q.append(c)

    return -1


for _ in range(M):  # 간선 정보 입력
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)  # 양방향이기 때문

ans = bfs(S, E)
print(ans)
