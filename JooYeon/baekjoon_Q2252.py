import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
indegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        result.append(cur)
        for i in graph[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for r in result:
        print(r, end=' ')

topology_sort()
