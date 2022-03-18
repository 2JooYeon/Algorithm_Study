import sys
from collections import deque
input = sys.stdin.readline


n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
distance = [-1] * (n+1)
distance[x] = 0


def bfs(x):
    queue = deque([x])
    while queue:
        cur = queue.popleft()
        for node in graph[cur]:
            if distance[node] == -1:
                distance[node] = distance[cur] + 1
                queue.append(node)
bfs(x)
flag = 1
for i in range(1, n+1):
    if distance[i] == k:
        flag = 0
        print(i)

if flag:
    print(-1)
