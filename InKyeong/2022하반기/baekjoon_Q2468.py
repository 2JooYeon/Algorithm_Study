n = int(input())

graph = [list(map(int, input().split(" "))) for _ in range(n)]
h = 0
for i in range(0, n) :
	if h <= max(graph[i]) :
		h = max(graph[i])

ans = 0
for i in range(h, 0, -1) :
	answer = 0
	g = [[1 if graph[x][y] <= i else 0 for y in range(0, n)] for x in range(0, n)]
	def dfs(x, y) :
		if x < 0 or y < 0 or x >= n or y >= n :
			return False
		if g[x][y] == 0 :
			g[x][y] = 1
			dfs(x + 1, y)
			dfs(x - 1, y)
			dfs(x, y + 1)
			dfs(x, y - 1)
			return True
		return False
	for x in range(0, n) :
		for y in range(0, n) :
			if dfs(x, y) : 
				answer += 1
	
	if ans <= answer : ans = answer

print(ans)


