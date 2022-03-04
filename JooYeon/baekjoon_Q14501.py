import sys
input = sys.stdin.readline

n = int(input())
term_price = []
d = [0 for _ in range(n+1)]
for _ in range(n):
    term_price.append(list(map(int, input().split())))

max_v = 0
for i in range(n-1, -1, -1):
    day = i + term_price[i][0]
    if day<=n:
        d[i] = max(term_price[i][1]+d[day], max_v)
        max_v = d[i]
    else:
        d[i] = max_v

print(d[0])
