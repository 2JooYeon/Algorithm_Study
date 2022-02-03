n = int(input())
unit = [3,5]
d = [10001]*(n+1)
d[0] = 0

for i in range(2):
    for j in range(unit[i], n+1):
        if d[j-unit[i]]!=1001:
            d[j] = min(d[j], d[j-unit[i]]+1)

if d[n] == 10001:
    print(-1)
else:
    print(d[n])
