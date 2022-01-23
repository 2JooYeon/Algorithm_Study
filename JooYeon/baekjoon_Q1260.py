import sys
from collections import deque


def make_graph(num_node, num_line):
    graph = [[] for _ in range(num_node + 1)]

    for _ in range(num_line):
        s_node, d_node = list(map(int, sys.stdin.readline().rstrip().split()))
        graph[s_node].append(d_node)
        graph[d_node].append(s_node)

    for data in graph:
        data.sort()

    return graph


def dfs(start, graph, visited):
    visited[start]=1
    print(start, end=' ')

    for node in graph[start]:
        if not visited[node]:
            dfs(node, graph, visited)


def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for node in graph[cur]:
            if not visited[node]:
                queue.append(node)
                visited[node] = 1


num_node, num_line, start = list(map(int, input().split()))
graph = make_graph(num_node, num_line)
visited_dfs = [0 for _ in range(num_node + 1)]
visited_bfs = [0 for _ in range(num_node + 1)]
dfs(start, graph, visited_dfs)
print()
bfs(start, graph, visited_bfs)
