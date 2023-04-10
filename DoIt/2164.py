from collections import deque
n = int(input())
myQueue = deque()

for i in range(1, n+1):  # 1부터 입력받은 수까지 카드 만들기
    myQueue.append(i)

while len(myQueue) > 1:
    myQueue.popleft()  # 한 장 버림
    myQueue.append(myQueue.popleft())  # 한 장 빼서 가장 아래로 이동

print(myQueue[0])
