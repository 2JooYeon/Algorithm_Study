from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    route = []
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    def bfs(start, graph, visited):
        count = 0
        q = deque()
        q.append((start, count))
        visited[start] = 1
        while q:
            node = q.popleft()
            cur = node[0]
            count = node[1]
            count += 1
            for v in graph[cur]:
                if not visited[v]:
                    route.append((count, v))
                    q.append((v, count))
                    visited[v] = 1
    bfs(1, graph, visited)
    route.sort(reverse=True)
    target = route[0][0]
    for r in route:
        if r[0] == target:
            answer += 1
    return answer
