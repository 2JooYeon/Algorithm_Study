import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]
maze = []
for _ in range(n):
    maze.append(list(map(int, input().rstrip())))

# 북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs():
    queue = deque([])
    queue.append([0,0])
    visited[0][0] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            if not visited[ny][nx] and maze[ny][nx]:
                visited[ny][nx] = 1
                maze[ny][nx] = maze[y][x] + 1
                queue.append([ny, nx])

bfs()
print(maze[n-1][m-1])
