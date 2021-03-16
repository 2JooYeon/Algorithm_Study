# 맞긴 맞았지만 시간이 너무 오래 걸림.
# from collections import Counter
#
# N = int(input())
#
# card = []
# for i in range(0,N):
#     card.append(int(input()))
#
# card_counter = Counter(card)
# print(sorted(card_counter.items(), key= lambda x: (x[1], -x[0]), reverse=True)[0][0])

import sys

N = int(input())

card = {}

for i in range(0,N):
    num = int(sys.stdin.readline().rstrip())
    if num in card:
        card[num] += 1
    else:
        card[num] = 1

print(sorted(card.items(), key= lambda x: (x[1], -x[0]), reverse=True)[0][0])