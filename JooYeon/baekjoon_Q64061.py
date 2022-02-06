def solution(board, moves):
    answer = 0
    n = len(board)
    bucket = []
    gamemap = [[] for _ in range(n+1)]
    for i in range(n):
        for row in board[::-1]:
            if row[i]:
                gamemap[i].append(row[i])

    for move in moves:
        move -= 1
        if gamemap[move]:
            cur = gamemap[move].pop()
            if bucket:
                target = bucket[-1]
                if cur == target:
                    answer += 2
                    bucket.pop()
                else:
                    bucket.append(cur)
            else:
                bucket.append(cur)
    return answer
