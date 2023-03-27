n = int(input())
word_list = [input() for _ in range(n)]

group_count = 0

for word in word_list:
    error = 0
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            word_ = word[i+1:]
            if word_.count(word[i]) > 0:
                error += 1

    if error == 0:
        group_count += 1

print(group_count)
