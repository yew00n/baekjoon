N = int(input())
num_list = list(map(int,input().split()))
min = num_list[0]
max = num_list[0]

for i in range(N):
    if min >= num_list[i]:
        min = num_list[i]
    if max <= num_list[i]:
        max = num_list[i]
    i += 1

print(min, max)