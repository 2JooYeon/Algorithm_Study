import sys
from collections import deque

n, m = list(map(int, input().split()))
graph = []
for _ in range(n):
    graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))

# 이동방향 정의 (상우하좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append([x,y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if n_x<0 or n_x>=n or n_y<0 or n_y>=m:
                continue
            if graph[n_x][n_y] == 1:
                graph[n_x][n_y] = graph[x][y] + 1
                queue.append([n_x, n_y])
    return graph[n-1][m-1]

print(bfs(0,0))
