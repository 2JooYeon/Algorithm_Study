import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
d = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

for i in range(1, len(str2)+1):
    for j in range(1, len(str1)+1):
        if str2[i-1] == str1[j-1]:
            d[i][j] = d[i-1][j-1]+1
        else:
            d[i][j] = max(d[i][j-1], d[i-1][j])

print(d[-1][-1])
