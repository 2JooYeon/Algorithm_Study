import sys

input = sys.stdin.readline

n = int(input())
ropes = []
weights = []

for i in range(n):
    ropes.append(int(input()))

ropes.sort(reverse=True)

for i in range(n):
    weights.append(ropes[i]*(i+1))

print(max(weights))