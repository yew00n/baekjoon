import sys

T = int(input()) 

for i in range(T):
    A, B = map(int, sys.stdin.readline().split()) #여러줄 입력받을 때 시간 단축
    print(A + B)
