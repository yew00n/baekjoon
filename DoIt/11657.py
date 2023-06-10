n, m = map(int, input().split())
route = [list(map(int, input().split())) for _ in range(m)]
dist = [1e9 for _ in range(n+1)]


def bel():
    dist[1] = 0
    for i in range(n):
        for cur, nex, weight in route:
            if dist[cur] != 1e9 and dist[nex] > dist[cur] + weight:
                dist[next] = dist[cur] + weight
                if i == n-1:
                    return True
        return False


if bel():
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] != 1e9:
            print(dist[i])
        else:
            print(-1)
