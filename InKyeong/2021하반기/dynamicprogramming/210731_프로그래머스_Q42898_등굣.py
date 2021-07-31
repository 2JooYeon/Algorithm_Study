def solution(m, n, puddles):
    answer = 0

    graph = [[0] * (m + 1) for _ in range(n + 1)]
    graph[1][1] = 1
    print(graph)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            elif [j, i] in puddles:
                graph[i][j] = 0
            else:
                graph[i][j] = graph[i - 1][j] + graph[i][j - 1]

    answer = graph[n][m] % 1000000007

    return answer