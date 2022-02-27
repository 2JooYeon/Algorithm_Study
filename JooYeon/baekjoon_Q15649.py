import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
per = permutations(range(1, n+1), m)
for line in per:
    for i in line:
        print(i, end=' ')
    print()
