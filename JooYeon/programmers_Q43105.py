def solution(triangle):
    answer = 0
    d = []

    for i in range(0, len(triangle)):
        d.append([-1]*len(triangle[-1]))

    for i in range(1, len(triangle)):
        for j in range(0, len(triangle[i])):
            d[i][j] = 0

    d[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(0, len(triangle[i])):
            if d[i-1][j-1]<0:
                d[i][j] = d[i-1][j] + triangle[i][j]
            elif d[i-1][j]<0:
                d[i][j] = d[i-1][j-1] + triangle[i][j]
            else:
                d[i][j] = max(d[i-1][j-1], d[i-1][j]) + triangle[i][j]

    answer = max(d[-1])
    return answer