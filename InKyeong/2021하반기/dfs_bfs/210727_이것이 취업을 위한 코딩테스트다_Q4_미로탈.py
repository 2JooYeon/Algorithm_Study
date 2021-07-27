from collections import deque
n, m = map(int, input().split())

graph = [[] for i in range(n)]

for i in range(0, n) :
    s = input()
    for j in range(0, m) :
        graph[i].append(int(s[j]))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :

    queue = deque()
    queue.append((x,y))

    while queue :
        x, y = queue.popleft()

        for i in range(0, 4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m :
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 :
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
                print(graph)

    return graph[n-1][m-1]

print(bfs(0, 0))
print(graph)


