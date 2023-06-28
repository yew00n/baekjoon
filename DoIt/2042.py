import sys
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = nums[start]
        return

    mid = (start + end) // 2
    init(start, mid, node*2)  # 왼쪽 자식 노드의 구간합
    init(mid+1, end, node*2 + 1)  # 오른쪽 자식 노드의 구간합

    tree[node] = tree[node*2] + tree[node*2 + 1]


def sum(L, R, node, nodeLeft, nodeRight):
    if R < nodeLeft or nodeRight < L:
        return 0

    if L <= nodeLeft and nodeRight <= R:
        return tree[node]

    mid = (nodeLeft + nodeRight) // 2
    return sum(L, R, node*2, nodeLeft, mid) + sum(L, R, node*2 + 1, mid+1, nodeRight)


def update(L, R, node, idx, val):
    if L == R == idx:  # 단일 구간 업데이트
        tree[node] = val
        return

    if idx < L or R < idx:
        return

    mid = (L + R) // 2
    update(L, mid, node*2, idx, val)  # 왼쪽 자식 노드 업데이트
    update(mid+1, R, node*2 + 1, idx, val)  # 오른쪽 자식 노드 업데이트
    # 업데이트된 자식 노드들을 더해서 현재 노드의 값에 저장
    tree[node] = tree[node*2] + tree[node*2 + 1]


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    nums = []
    tree = [0 for _ in range(N*4)]

    for _ in range(N):
        nums.append(int(input()))

    init(0, N-1, 1)

    for _ in range(M+K):
        a, b, c = map(int, input().split())

        if a == 1:
            b -= 1
            update(0, N-1, 1, b, c)
        else:
            b -= 1
            c -= 1
            print(sum(b, c, 1, 0, N-1))
