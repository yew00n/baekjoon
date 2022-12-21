hour, min = map(int, input().split())
add_min = int(input())

# +=, -+ 사용할 때는 변수 지정 순서에 주의
extra_hour = (min + add_min) // 60
min = (min + add_min) % 60
hour = hour + extra_hour

if hour >= 24:
    hour -= 24

print(hour, min)

