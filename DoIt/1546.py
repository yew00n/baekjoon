n = int(input())
score_list = list(map(int, input().split()))

max = 0
total_score = 0

for score in score_list:
    if max < score:
        max = score
    total_score += score

print(total_score*100/max/n)
