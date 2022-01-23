import sys
from collections import deque
m, n = list(map(int, input().split()))
graph = []
queue = deque()

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

# 이동정보 설정하기(상우하좌)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs():
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            n_x = x+dx[i]
            n_y = y+dy[i]
            if n_x<0 or n_x>=m or n_y<0 or n_y>=n:
                continue
            if graph[n_y][n_x] == 0:
                graph[n_y][n_x] = graph[y][x] + 1
                queue.append([n_y, n_x])

bfs()
state = 0
for i in range(n):
    if 0 in graph[i]:
        state = 0
        break
    state = max(max(graph[i]), state)
if state == 1:
    print(0)
else:
    print(state-1)
