import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

x, k = map(int, input().split())

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

answer = graph[1][k]+graph[k][x]
if answer < INF:
    print(answer)
else:
    print(-1)
