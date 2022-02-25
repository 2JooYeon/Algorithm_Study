import sys

input = sys.stdin.readline

n = int(input())
tri = []
d = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    tri.append(list(map(int, input().split())))
num = 2
d[0][0] = tri[0][0]

for i in range(1, n):
    for j in range(num):
        if 0 < j and j < (num - 1):
            d[i][j] = max(d[i - 1][j - 1] + tri[i][j], d[i - 1][j] + tri[i][j])
        elif j == 0:
            d[i][j] = d[i - 1][j] + tri[i][j]
        elif j == num - 1:
            d[i][j] = d[i - 1][j - 1] + tri[i][j]
    num += 1
print(max(d[n - 1]))
