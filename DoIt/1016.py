# 일반 반복문 쓰면 시간 초과됨
import math
min, max = map(int, input().split())
check = [False] * (max-min+1)

answer = max - min + 1

for i in range(2, int(math.sqrt(max)+1)):
    square = i**2
    for j in range((((min-1)//square)+1)*square, max+1, square):  # 제곱수
        if not check[j-min]:
            check[j-min] = True
            answer -= 1
print(answer)
