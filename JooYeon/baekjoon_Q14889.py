import sys
from itertools import combinations, permutations
input = sys.stdin.readline

n = int(input())
mem = range(n)
s = []
answer = 1e9
for _ in range(n):
    s.append(list(map(int, input().split())))

combi = combinations(mem, n//2)
for c in combi:
    start = permutations(c, 2)
    link = permutations((set(mem) - set(c)), 2)
    start_sum = 0
    link_sum = 0
    for i, j in start:
        start_sum += s[i][j]
    for i, j in link:
        link_sum += s[i][j]
    answer = min(answer, abs(start_sum - link_sum))
print(answer)
