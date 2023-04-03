n = int(input())
sum, count, start_index, end_index = 1, 1, 1, 1

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        start_index += 1
        sum -= (start_index-1)
    elif sum < n:
        end_index += 1
        sum += end_index
print(count)
