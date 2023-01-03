natural_numbers = set(range(1, 10001))
generated_numbers = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j) #원래 숫자 + 각 자릿수의 숫자
    generated_numbers.add(i)

self_numbers = sorted(natural_numbers - generated_numbers)

for i in self_numbers:
    print(i)