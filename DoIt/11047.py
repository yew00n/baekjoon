import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = [0]*n

for i in range(n):  # 이미 오름차순으로 주어지는 경우
    a[i] = int(input())

count = 0
for i in range(n-1, -1, -1):
    if a[i] <= k:
        count += int(k/a[i])
        k = k % a[i]

print(count)
