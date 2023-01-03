num_list = [input() for _ in range(9)] #input several number of rows
# max = num_list[0]

# for i in range(len(num_list)-1):
#     if max <= num_list[i]:
#         max = num_list[i]
#         row = i+1
#     i += 1

# print(max)
# print(row)

print(max(num_list))
print(num_list.index(max(num_list))+1)