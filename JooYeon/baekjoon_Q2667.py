import sys

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))
global count
count = 0


def dfs(i, j, graph):
    if i < 0 or i >= n or j < 0 or j >= n:
        return False

    if graph[i][j] == 1:
        global count
        count += 1
        graph[i][j] = 0
        # 상
        dfs(i, j-1, graph)
        # 우
        dfs(i+1, j, graph)
        # 하
        dfs(i, j+1, graph)
        # 좌
        dfs(i-1, j, graph)
        return True

    return False

answer = []
for i in range(n):
    for j in range(n):
        count = 0
        if dfs(i, j, graph):
            answer.append(count)
print(len(answer))
answer.sort()
for num in answer:
    print(num)
