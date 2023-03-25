import sys
def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
buckets = [i for i in range(1, n+1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    i, j, k = i-1, j-1, k-1
    a, b, c = buckets[k:j+1], buckets[i:k + 1], buckets[j+1: len(buckets)+1]
    buckets = a + b + c

print(*buckets)
