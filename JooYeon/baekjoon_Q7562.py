import sys
from collections import deque
input = sys.stdin.readline


# 문제에서 주어진 이동 방향
dx = [1,2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2,2,1,-1,-2]
def bfs(x, y, l, tar_x, tar_y):
    visited = [[0 for _ in range(l)] for _ in range(l)]
    queue = deque()
    queue.append([x,y,0])
    visited[y][x] = 1
    while queue:
        cur_x, cur_y, count = queue.popleft()
        for i in range(8):
            n_x = cur_x + dx[i]
            n_y = cur_y + dy[i]
            if n_x<0 or n_y<0 or n_x>=l or n_y>=l:
                continue
            if n_x == tar_x and n_y == tar_y:
                return count+1
            if visited[n_y][n_x] == 0:
                visited[n_y][n_x] = 1
                queue.append([n_x, n_y, count+1])


t = int(input())
answer = []
for _ in range(t):
    l = int(input())
    s_i, s_j = map(int, input().split())
    e_i, e_j = map(int, input().split())
    if s_i==e_i and s_j==e_j:
        answer.append(0)
    else:
        answer.append(bfs(s_i, s_j, l, e_i, e_j))
for a in answer:
    print(a)
