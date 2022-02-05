import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] or (graph[i][k] and graph[k][j]):
                graph[i][j] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()

