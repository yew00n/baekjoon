N, X = map(int,input().split())
num_list1 = list(map(int,input().split()))
# num_list2 = []
smaller_numbers = ''

for i in range(N):
    if num_list1[i] < X:
        smaller_numbers = smaller_numbers + ' ' + str(num_list1[i])
        # num_list2.append(num_list1[i])
        i += 1
    else:
        i += 1

print(smaller_numbers.lstrip())
        