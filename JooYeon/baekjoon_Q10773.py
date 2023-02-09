import sys
input = sys.stdin.readline

k = int(input())
q = []
for _ in range(k):
    n = int(input())
    if n:
        q.append(n)
    else:
        if len(q):
            q.pop()

print(sum(q))
