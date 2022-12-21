import sys

#정수 1개 입력받기
a = int(sys.stdin.readline().rstrip())
print(a)

#정수 여러개 입력받기
a, b, c = map(int, sys.stdin.readline().rstrip().split())
print(a, b, c)

#입력받은 정수 여러개를 리스트에 저장하기
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
print(num_list)

#정수 n개를 입력받아 2차원 리스트에 저장하기
n = int(sys.stdin.readline().rstrip())
num_list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
print(num_list)
