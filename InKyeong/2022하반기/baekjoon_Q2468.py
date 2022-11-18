from collections import deque
import copy

N = int(input())

graph = [list(map(int, input().split(" "))) for _ in range(N)]

h = 0
for i in range(0, N) :
	if h <= max(graph[i]) :
		h = max(graph[i])

def bfs(graph, x, y, height) :
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	queue = deque()
	queue.append([x, y])
	cnt = 0
	while queue :
		x, y = queue.popleft()

		for i in range(0, 4) :
			newX, newY = x + dx[i], y + dy[i]
			if newX < 0 or newY < 0 or newX >= N or newY >= N :
				continue
			if graph[newX][newY] == 0 :
				cnt += 1
			if graph[newX][newY] <= height :
				continue
			if graph[newX][newY] > height :
				queue.append([newX, newY])
				graph[newX][newY] = 0

	return cnt

count = 0

for k in range(1, h):
	g = copy.deepcopy(graph)
	for i in range(N):
		for j in range(N):
			if g[i][j] <= k :
				ans = bfs(g,i,j,k)
				if ans > 0 :
					print(ans)

	print(k, "!!", g)
