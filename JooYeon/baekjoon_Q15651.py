import sys
from itertools import product
input = sys.stdin.readline

n, m = map(int, input().split())
per = product(range(1, n+1), repeat = m)
for line in per:
    print(' '.join(map(str, list(line))))
