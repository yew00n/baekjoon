n, m = map(int, input().split())
a = list(map(int, input().split()))
start = 0
end = 0

for i in a:
    if start < i:
        start = i
    end += i

while start <= end:
    mid = int((start+end)/2)
    sum = 0
    count = 0
    for i in range(n):
        if sum + a[i] > mid:
            count += 1
            sum = 0
        sum += a[i]
    if sum != 0:
        count += 1
    if count > m:
        start = mid + 1
    else:
        end = mid - 1
