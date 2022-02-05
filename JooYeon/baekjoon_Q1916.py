'''다익스트라 알고리즘'''
import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리된 적 있는 노드면 무시
        if distance[now]<dist:
            continue
        # 현재 노드의 인접 노드 확인
        for nodes in graph[now]:
            # nodes --> (도착노드, 가중치)
            cost = dist + nodes[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는게 더 짧은 경우
            if cost < distance[nodes[0]]:
                distance[nodes[0]] = cost
                heapq.heappush(q, (cost, nodes[0]))

start, end = map(int, input().split())
dijkstra(start)
print(distance[end])
