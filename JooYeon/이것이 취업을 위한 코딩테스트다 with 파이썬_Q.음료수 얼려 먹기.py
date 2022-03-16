import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]
ice_map = []
for _ in range(n):
    ice_map.append(list(map(int, input().rstrip())))


# 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def dfs(y, x):
    if y<0 or x<0 or y>=n or x>=m:
        return False
    if not visited[y][x] and not ice_map[y][x]:
        visited[y][x] = 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(ny, nx)
        return True
    return False


answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer += 1
print(answer)
