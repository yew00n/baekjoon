N, M = map(int, input().split())
knows_true = list(map(int, input().split()))
T = knows_true[0]
del knows_true[0]
result = 0
party = [[] for _ in range(M)]


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


def check_same(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False


for i in range(M):
    party[i] = list(map(int, input().split()))
    del party[i][0]

parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i

for i in range(M):
    first_p = party[i][0]
    for j in range(1, len(party[i])):
        union(first_p, party[i][j])

for i in range(M):
    is_possible = True
    first_p = party[i][0]
    for j in range(len(knows_true)):
        if find(first_p) == find(knows_true[j]):
            is_possible = False
            break
    if is_possible:
        result += 1

print(result)
