import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = [[0,0] for _ in range(n+1)]
for i in range(1,n+1):
    data[i] = list(map(int, input().split()))
d = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j>=data[i][0]:
            d[i][j] = max(d[i-1][j], d[i-1][j-data[i][0]]+data[i][1])
        else:
            d[i][j] = d[i-1][j]

print(d[-1][-1])
