import sys
from collections import deque

m, n, h = map(int, input().split())
graph = []
queue = deque()
for k in range(h):
    graph.append([])
    for i in range(n):
        graph[k].append(list(map(int, sys.stdin.readline().rstrip().split())))
        for j in range(m):
            if graph[k][i][j] == 1:
                queue.append([k, i, j])


# 이동 정보 설정하기
dh = [0, 0, 0, 0, -1, 1]
dy = [-1, 0, 1, 0, 0, 0]
dx = [0, 1, 0, -1, 0, 0]

while queue:
    z, y, x = queue.popleft()
    for i in range(6):
        n_z = z + dh[i]
        n_y = y + dy[i]
        n_x = x + dx[i]
        if n_z<0 or n_z>=h or n_y<0 or n_y>=n or n_x<0 or n_x>=m:
            continue
        if graph[n_z][n_y][n_x] == 0:
            graph[n_z][n_y][n_x] = graph[z][y][x] + 1
            queue.append([n_z, n_y, n_x])

state = 0
for k in range(h):
    for i in range(n):
        if 0 in graph[k][i]:
            print(-1)
            exit(0)
        state = max(max(graph[k][i]), state)

if state == 1:
    print(0)
else:
    print(state-1)
