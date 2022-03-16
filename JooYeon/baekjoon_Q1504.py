import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
distance = [INF] * (n + 1)

def dijkstra(start):
    global distance
    distance = [INF] * (n + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, cur = heapq.heappop(queue)
        if distance[cur]<dist:
            continue
        for dest, money in graph[cur]:
            cost = dist + money
            if cost < distance[dest]:
                distance[dest] = cost
                heapq.heappush(queue, (cost, dest))

dijkstra(1)
dist_v1 = distance[v1]
dist_v2 = distance[v2]

dijkstra(v1)
v1_end = distance[n]
v1_v2 = distance[v2]

dijkstra(v2)
v2_end = distance[n]
v2_v1 = distance[v1]

answer = min(dist_v1+v1_v2+v2_end, dist_v2+v2_v1+v1_end)
if answer < INF:
    print(answer)
else:
    print(-1)
