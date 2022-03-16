import sys
input = sys.stdin.readline

n, m = map(int, input().split())
unit = []
for _ in range(n):
    unit.append(int(input().rstrip()))
d = [int(1e9)] * (m+1)
d[0] = 0

for i in range(n):
    for j in range(unit[i], m+1):
        d[j] = min(d[j], d[j-unit[i]]+1)
if d[m] == int(1e9):
    print(-1)
else:
    print(d[m])
