import sys
sys.setrecursionlimit(3000)

def dfs(i, j, m, n, graph):
    if i<0 or i>=m or j<0 or j>=n:
        return False

    if graph[j][i] == 1:
        graph[j][i] = 0
        # 상
        dfs(i, j-1, m, n, graph)
        # 우
        dfs(i+1, j, m, n, graph)
        # 하
        dfs(i, j+1, m, n, graph)
        # 좌
        dfs(i-1, j, m, n, graph)
        return True

    return False


answer = []
num_t = int(input())

for _ in range(num_t):
    count = 0
    m, n, k = list(map(int, input().split()))
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = list(map(int, sys.stdin.readline().rstrip().split()))
        graph[y][x] = 1

    for i in range(m):
        for j in range(n):
            if dfs(i, j, m, n, graph):
                count += 1

    answer.append(count)

for num in answer:
    print(num)
