import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))
lines.sort()
d = [lines[0][1]]
for i in range(1,n):
    if lines[i][1]>d[-1]:
        d.append(lines[i][1])
    elif lines[i][1]<d[-1]:
        left = bisect_left(d, lines[i][1])
        d[left] = lines[i][1]
print(n-len(d))
