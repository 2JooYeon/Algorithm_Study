def solution(triangle):
    lennum = len(triangle)

    d = []
    for i in range(0, lennum):
        k = [0] * (i + 1)
        d.append(k)

    d[0][0] = triangle[0][0]
    d[1][0] = d[0][0] + triangle[1][0]
    d[1][1] = d[0][0] + triangle[1][1]
    answer = 0

    for i in range(2, lennum):
        for j in range(0, i + 1):

            if j == 0:
                d[i][j] = d[i - 1][j] + triangle[i][j]
            elif j == i:
                d[i][j] = d[i - 1][j - 1] + triangle[i][j]
            else:
                d[i][j] = max(d[i - 1][j - 1], d[i - 1][j]) + triangle[i][j]

            answer = max(answer, d[i][j])

    return answer