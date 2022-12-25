count = 0
N = int(input())
num_list = list(map(int, input().split()))
find = int(input())

for i in range(N): #starts from i=0
    if find == num_list[i]:
        count += 1
        i += 1
    else:
        i += 1

print(count)
    
