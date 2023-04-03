import sys
input = sys.stdin.readline
numNo, quizNo = map(int, input().split())
num_list = list(map(int, input().split()))
sum_list = [0]
# sum_list[0] != 0 이면 이후 sum_list[i-2]에서 i=1일 때 배열의 가장 마지막 인덱스로 넘어감
sum = 0

for num in num_list:
    sum += num
    sum_list.append(sum)

for _ in range(quizNo):
    i, j = map(int, input().split())
    print(sum_list[j]-sum_list[i-1])
