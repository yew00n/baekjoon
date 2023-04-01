a = [[0] * 15 for _ in range(5)]

for i in range(5):
    b = list(input())
    for j in range(len(b)):
        a[i][j] = b[j]

for i in range(15):
    for j in range(5):
        if a[j][i] == 0:
            continue
        else:
            print(a[j][i], end='')
