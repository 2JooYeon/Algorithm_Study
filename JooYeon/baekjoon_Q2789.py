from itertools import combinations
n, m = list(map(int, input().split()))
cards = list(map(int, input().split()))
result = list(combinations(cards, 3))
answer = 0
for comb in result:
    target = sum(comb)
    if target <= m:
        answer = max(answer, target)
print(answer)
