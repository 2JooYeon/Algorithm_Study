import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e,c))

def dijkstra(start):
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
    return distance

go_home = dijkstra(x)
answer = []
for i in range(1, n+1):
    temp = dijkstra(i)
    answer.append(go_home[i]+temp[x])
print(max(answer))
