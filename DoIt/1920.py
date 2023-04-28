n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
target_list = list(map(int, input().split()))

for i in range(m):
    find = False
    target = target_list[i]

    start = 0
    end = len(a) - 1
    while start <= end:
        midi = int((start + end)/2)
        midv = a[midi]
        if midv > target:
            end = midi - 1
        elif midv < target:
            start = midi + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)
