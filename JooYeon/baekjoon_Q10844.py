import sys
input = sys.stdin.readline

n = int(input())
d = [[0 for _ in range(10)] for _ in range(n+1)]
d[1][0] = 0
d[1][1:] = [1] * 9
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i-1][j+1]
        elif j == 9:
            d[i][j] = d[i-1][j-1]
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]

print(sum(d[n])%1000000000)
