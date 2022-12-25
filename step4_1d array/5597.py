submit_list = [input() for _ in range(28)]
unsubmit_list = list(range(1,31))
i = 1

while i <= len(unsubmit_list):
    print("checking: ", i)
    for j in range(len(submit_list)):
        print("comparing: ", submit_list[j], unsubmit_list[i-1])
        if submit_list[j] == unsubmit_list[i-1]:
            print("   matched", submit_list[j], unsubmit_list[i-1])
            del unsubmit_list[i-j]
        j += 1
    i += 1

print(unsubmit_list)
print(min(unsubmit_list))
print(max(unsubmit_list))