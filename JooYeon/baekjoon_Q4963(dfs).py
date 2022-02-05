import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)

# 북쪽 방향부터 시계방향으로 이동
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def dfs(i, j, graph, visited, w, h):
    if i<0 or i>=h or j<0 or j>=w:
        return False
    if graph[i][j] and not visited[i][j]:
        visited[i][j] = 1
        for k in range(8):
            ny = i + dy[k]
            nx = j + dx[k]
            dfs(ny, nx, graph, visited, w, h)
        return True
    return False


answer = []
while 1:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    graph = [[] for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        graph[i] = list(map(int, input().split()))
    count = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j, graph, visited, w, h):
                count += 1
    answer.append(count)

for a in answer:
    print(a)
