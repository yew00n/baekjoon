import sys
import heapq
n = int(input())
card_deck = []

for _ in range(n):
    heapq.heappush(card_deck, int(sys.stdin.readline()))


group1 = 0
group2 = 0
sum = 0

while len(card_deck) > 1:
    group1 = heapq.heappop(card_deck)
    group2 = heapq.heappop(card_deck)
    temp = group1 + group2
    sum += temp
    heapq.heappush(card_deck, temp)

print(sum)
