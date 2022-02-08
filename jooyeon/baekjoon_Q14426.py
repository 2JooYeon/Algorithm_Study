import sys

answer = 0
input = sys.stdin.readline
n, m = map(int, input().split())
s = []
target = []

for i in range(n):
    s.append(input().rstrip())

for i in range(m):
    target.append(input().rstrip())

for word in target:
    for w in s:
        if w.startswith(word):
            answer += 1
            break

print(answer)
