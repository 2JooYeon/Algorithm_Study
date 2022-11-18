from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
  graph.append(list(map(int, input())))

queue = deque()
queue.append([0, 0])
def bfs() :
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	while queue :
		x, y = queue.popleft()
		for i in range(0, 4) :
			newx, newy = x + dx[i], y + dy[i]
			if newx < 0 or newy < 0 or newx >= n or newy >= m :
				continue
			if graph[newx][newy] == 0 :
				continue
			if graph[newx][newy] == 1 :
				graph[newx][newy] = graph[x][y] + 1
				queue.append([newx, newy])
	return graph[n - 1][m - 1]

print(bfs())