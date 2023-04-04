import sys
input = sys.stdin.readline

matNum = int(input())
aimNum = int(input())
matList = list(map(int, input().split()))
matList.sort()

count = 0
start_index = 0
end_index = aimNum - 1
# sum = matList[start_index] + matList[end_index]

while start_index < end_index:
    if matList[start_index] + matList[end_index] < aimNum:
        start_index += 1
        # sum = matList[start_index] + matList[end_index]
    elif matList[start_index] + matList[end_index] > aimNum:
        end_index -= 1
        # sum = matList[start_index] + matList[end_index]
    else:
        start_index += 1
        end_index -= 1
        # sum = matList[start_index] + matList[end_index]
        count += 1

print(count)
