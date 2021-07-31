from collections import deque


def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n + 1)]

    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                continue
            elif computers[i][j] == 1:
                graph[i + 1].append(j + 1)

    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if visited[i] == True:
            continue
        if visited[i] == False:
            answer += 1
            bfs(graph, i, visited)

    return answer


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

