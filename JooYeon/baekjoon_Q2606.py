import sys
from collections import deque

def bfs(start, graph, visited):
    count = 0
    queue = deque([start])
    visited[start] = 1
    while queue:
        cur = queue.popleft()
        count += 1
        for node in graph[cur]:
            if not visited[node]:
                queue.append(node)
                visited[node] = 1
    return count-1

n = int(input())
l = int(input())
visited = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(l):
    node1, node2 = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[node1].append(node2)
    graph[node2].append(node1)

print(bfs(1, graph, visited))
