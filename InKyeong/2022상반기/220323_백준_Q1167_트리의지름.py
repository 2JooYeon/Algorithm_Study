vertex = int(input())
graph = [ [] for _ in range (vertex + 1) ]

for _ in range (vertex) :
	c = list(map(int, input().split()))
	for e in range(1, len(c) - 2, 2):
		graph[c[0]].append((c[e], c[e + 1]))

#dfs 들어가서 배열에 도착하는 곳까지의 거리 저장
def dfs(v,result):
	for a, b in graph[v]:
		if result[a] == -1:
			result[a] = result[v] + b
			dfs(a,result)

#임의의 점에서 최대 거리 저장
result1 = [-1] * (vertex + 1)
result1[1] = 0
dfs(1, result1)

temp = 0
index = 0
#최대값일때의 인덱스값을 찾음
for i in range(1, len(result1)):
	if result1[i] > temp:
		temp = result1[i]
		index = i
#그 인덱스에서 시작하는 최대값 찾음
result2 = [-1] * (n+1)
result2[index] = 0
dfs(index, result2)
print(max(result2))
