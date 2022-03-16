import sys
input = sys.stdin.readline

n, m = map(int, input().split())
y, x, direction = map(int, input().split())

game_map = []
# 0: 육지, 1: 바다
for _ in range(n):
    game_map.append(list(map(int, input().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]
visited[y][x] = 1

# 북, 동, 남, 서 (시계 방향)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

answer = 1
turn = 0

def turn_left():
    global direction
    direction -= 1
    if direction < 0:
        direction = 3

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if game_map[ny][nx] == 0 and not visited[ny][nx]:
        x = nx
        y = ny
        visited[ny][nx] = 1
        answer += 1
        turn = 0
    else:
        turn += 1
    if turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if game_map[ny][nx]:
            break
        else:
            x = nx
            y = ny
            turn = 0

print(answer)
