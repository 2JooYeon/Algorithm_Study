import sys
input = sys.stdin.readline

v, e = map(int, input().split())
edges = []
parents = [0 for _ in range(v+1)]
answer = 0
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

for i in range(1, v+1):
    parents[i] = i


def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, x, y):
    x = find_parent(parents, x)
    y = find_parent(parents, y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

edges.sort()

for edge in edges:
    c, a, b = edge
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        answer += c

print(answer)
