import sys
input = sys.stdin.readline

n = int(input())
stair = []
d = [0]*301

for i in range(n):
    stair.append(int(input()))

d[0] = stair[0]
if n>1:
    d[1] = sum(stair[:2])
if n>2:
    d[2] = max(stair[0]+stair[2], sum(stair[1:3]))
for i in range(3, n):
    d[i] = max(d[i-3]+stair[i-1]+stair[i], d[i-2]+stair[i])
print(d[n-1])
