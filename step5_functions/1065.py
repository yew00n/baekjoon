def hansu(n):
    cnt = 0
    for i in range(1, n+1):
        digit_number = list(map(int, str(i)))
        if i <= 99:
            cnt += 1
        elif digit_number[0]-digit_number[1] == digit_number[1]-digit_number[2]:
            cnt += 1
    return cnt

x = int(input())
print(hansu(x))