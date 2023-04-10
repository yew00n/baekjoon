from queue import PriorityQueue
import sys
print = sys.stdout.write  # 개행문자없이 출력
input = sys.stdin.readline
n = int(input())
myQueue = PriorityQueue()

for i in range(n):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str(temp[1])+'\n')
    else:
        myQueue.put((abs(request), request))  # put: 큐에 더하기, (우선순위, 값)
