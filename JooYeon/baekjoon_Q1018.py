import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input().rstrip()))

case1 = list('WBWBWBWB')
case2 = list('BWBWBWBW')

count = 1e9

def count_draw(color, y, x):
    countW = 0
    for i in range(8):
        if i % 2 == 0:
            temp = zip(case1, board[y+i][x:])
            for a,b in temp:
                if a!= b:
                    countW += 1
        else:
            temp = zip(case2, board[y + i][x:])
            for a,b in temp:
                if a!= b:
                    countW += 1
    countB = 0
    for i in range(8):
        if i % 2 == 0:
            temp = zip(case2, board[y+i][x:])
            for a,b in temp:
                if a!= b:
                    countB += 1
        else:
            temp = zip(case1, board[y + i][x:])
            for a,b in temp:
                if a!= b:
                    countB += 1
    return min(countW, countB)

for i in range(n-8+1):
    for j in range(m-8+1):
        check = board[i][j]
        count = min(count, count_draw(check, i, j))
print(count)
