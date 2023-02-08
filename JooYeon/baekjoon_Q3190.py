import sys
input = sys.stdin.readline

answer = 0
# 이동 방향 정보 (y,x) 기준 / e, s, w, n
rotate = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 처음에는 동쪽 방향
dir = 0

n = int(input())
board = [[0]*(n+1) for _ in range(n+1)]
k = int(input())

for i in range(k):
    y, x = map(int, input().split())
    # 사과 있는 곳은 1로 표시
    board[y][x] = 1

l = int(input())
moves = []


for i in range(l):
    data = input()
    s, m = int(data.split()[0]), data.split()[1]
    moves.append([s, m])

# 뱀이 위치한 곳은 -1로 표시
y, x = 1, 1
board[y][x] = -1
time = 0
# 회전할 인덱스
rotate_index = 0

# board에서 뱀의 현재 위치
q = [(y,x)]
while True:
    # 이동하기
    y += rotate[dir][0]
    x += rotate[dir][1]
    # 벽 부딪히는지 확인, 자기 몸이랑 부딪히는지 확인
    if x < 1 or y < 1 or x > n or y > n or board[y][x] == -1:
        time += 1
        break
    # 안 부딪혔으면
    else:
        # 사과 있을 경우
        if board[y][x] == 1:
            board[y][x] = -1
            q.append([y, x])
        # 사과 없을 경우
        if board[y][x] == 0:
            board[y][x] = -1
            q.append([y, x])
            ty, tx = q.pop(0)
            board[ty][tx] = 0
    time += 1
    # 회전할 시간인지 확인
    if rotate_index < l and time == moves[rotate_index][0]:
        m = moves[rotate_index][1]
        if m == 'L':
            dir = (dir - 1) % 4
        else:
            dir = (dir + 1) % 4
        rotate_index += 1

print(time)