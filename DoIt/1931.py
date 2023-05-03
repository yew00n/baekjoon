n = int(input())
a = [[0]*2 for _ in range(n)]

for i in range(n):
    s, e = map(int, input().split())
    a[i][0] = e
    a[i][1] = s

a.sort()
count = 0
end = -1

for i in range(n):
    if a[i][1] >= end:
        end = a[i][0]
        count += 1

print(count)
