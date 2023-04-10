n = int(input())
# answer = [0]*n
answer = [-1]*n
A = list(map(int, input().split()))
myStack = []

myStack.append(0)  # stack에는 index를 저장
for i in range(n):
    while myStack and A[myStack[-1]] < A[i]:  # myStack[-1] = myStack[top]
        answer[myStack.pop()] = A[i]  # 오큰수 저장
    myStack.append(i)

# while myStack:  # 반복문을 다 돌아도 스택이 비어있지 않다면
#     answer[myStack.pop()] = -1

print(*answer)
