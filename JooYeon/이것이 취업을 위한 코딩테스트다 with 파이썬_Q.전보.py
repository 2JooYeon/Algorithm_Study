import sys
import heapq
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

distance = [int(1e9)] * (n+1)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, cur = heapq.heappop(queue)
        if distance[cur] < dist:
            continue
        for destination, money in graph[cur]:
            cost = dist + money
            if cost < distance[destination]:
                distance[destination] = cost
                heapq.heappush(queue, (cost, destination))

dijkstra(c)

count = 0
max_dist = 0
for d in distance:
    if d != int(1e9):
        count += 1
        max_dist = max(max_dist, d)

print(count-1, max_dist)
