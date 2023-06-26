import sys
input = sys.stdin.readline
N, M = map(int, input().split())
text_list = set([input() for _ in range(N)])
count = 0

for _ in range(M):
    sub_text = input()
    print("~~~", sub_text)
    if sub_text in text_list:
        count += 1

print(count)
