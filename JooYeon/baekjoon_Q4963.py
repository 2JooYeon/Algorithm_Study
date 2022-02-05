import sys
input = sys.stdin.readline
from collections import deque

# 북 방향 부터 시계방향으로 이동 (북, 북동, 동, 동남, 남, 남서, 서, 서북)
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def bfs(i, j, graph, visited, w, h):
    queue = deque()
    visited[i][j] = 1
    queue.append([i, j])
    while queue:
        y, x = queue.popleft()
        for k in range(8):
            ny = y + dy[k]
            nx = x + dx[k]
            if ny<0 or ny>=h or nx<0 or nx>=w:
                continue
            if graph[ny][nx] and not visited[ny][nx]:
                queue.append([ny, nx])
                visited[ny][nx] = 1

answer = []
while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [[] for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    count = 0
    for i in range(h):
        graph[i] = list(map(int, input().rstrip().split()))
    for i in range(h):
        for j in range(w):
            if graph[i][j] and not visited[i][j]:
                bfs(i, j, graph, visited, w, h)
                count += 1
    answer.append(count)

for a in answer:
    print(a)
