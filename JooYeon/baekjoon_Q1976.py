import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a


n = int(input().rstrip())
m = int(input().rstrip())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(i+1, n+1):
        if graph[i-1][j-1]:
            union_parent(parent, i, j)

result = []
plan = list(map(int, input().split()))
for city in plan:
    result.append(find_parent(parent, city))
result = set(result)
if len(result) == 1:
    print('YES')
else:
    print('NO')
