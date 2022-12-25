count = 1
x = int(input())

ten = x//10
one = x%10
new = (one*10)+(ten+one)%10

while x != new:
    ten = new//10
    one = new%10
    new = (one*10)+(ten+one)%10
    count += 1

print(count)
