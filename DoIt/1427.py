import sys
print = sys.stdout.write

numList = list(input())

for i in range(len(numList)):
    max = i
    for j in range(i+1, len(numList)):
        if numList[j] > numList[max]:
            max = j
    if numList[i] < numList[max]:
        temp = numList[i]
        numList[i] = numList[max]
        numList[max] = temp

for i in range(len(numList)):
    print(numList[i])
