import math
n = int(input())
A = [0]*1000001

for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A)))):
    if A[i] == 0:
        continue
    for j in range(i+i, len(A), i):  # 2배수부터 시작해서 배수를 쭉 지움
        A[j] = 0


status = False


def pelin(target):  # 팰린드롬 수 판별
    temp = list(str(target))
    # num_list = list(str(num).split())
    s, e = 0, len(temp)-1

    while (s < e):
        if temp[s] != temp[e]:
            return False
        s += 1
        e -= 1
    return True


i = n
while True:
    if A[i] != 0:  # 소수이고
        if (pelin(A[i])):  # 팰린드롬 수
            print(A[i])
            break
        i += 1
