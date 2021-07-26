from collections import deque

N, L, S = input().split()
N = int(N)
L = int(L)
S = int(S)
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
graph = [ [] for i in range(N+1) ]
# print(graph)

for i in range(0, L):
    a, b = input().split()
    a = int(a)
    b = int(b)
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()
    
print(graph)


def dfs(graph, S, visited_dfs):
    visited_dfs[S] = True
    print(S, end = ' ')
    for i in graph[S] :
        if not visited_dfs[i] :
            dfs(graph, i, visited_dfs)

dfs(graph, S, visited_dfs)
print()

def bfs(graph, S, visited_bfs):
    queue = deque([S])

    visited_bfs[S] = True

    while queue :
        v = queue.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

bfs(graph, S, visited_bfs)