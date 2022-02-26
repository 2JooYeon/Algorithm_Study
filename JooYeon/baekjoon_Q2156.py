import sys
input = sys.stdin.readline

n = int(input())
grapes = [0] * 10001
for i in range(n):
    grapes[i] = int(input())

d = [0] * 10001
d[0] = grapes[0]
d[1] = grapes[0] + grapes[1]
d[2] = max(grapes[0]+grapes[2], grapes[1]+grapes[2], d[1])
for i in range(3,n):
    d[i] = max(d[i-2]+grapes[i], d[i-3]+grapes[i-1]+grapes[i], d[i-1])
print(max(d))
