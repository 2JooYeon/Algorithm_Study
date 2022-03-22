from collections import deque

vertex = int(input())
graph = [ [] for _ in range (vertex + 1) ]

for _ in range (vertex) :
	c = list(map(int, input().split()))
	for e in range(1, len(c) - 2, 2):
		graph[c[0]].append((c[e], c[e + 1]))


