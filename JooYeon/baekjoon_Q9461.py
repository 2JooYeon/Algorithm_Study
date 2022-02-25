import sys
input = sys.stdin.readline

d = [0] * 101
t = int(input())
n = []
for _ in range(t):
    n.append(int(input()))
d[1:6] = [1,1,1,2,2]
target = max(n)
for i in range(6, target+1):
    d[i] = d[i-1] + d[i-5]
for i in n:
    print(d[i])
