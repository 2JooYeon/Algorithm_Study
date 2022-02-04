import sys
input = sys.stdin.readline
import heapq

# 저점 개수, 간선 개수
v, e = map(int, input().split())

# 시작노드
start = int(input())

# 무한
INF = int(1e9)

# 노드 연결 정보 저장할 리스트
graph = [[] * (v+1) for _ in range(v+1)]
# 최단 거리 테이블
distance = [INF] * (v+1)

# 노드 연결 정보 받기
for _ in range(e):
    a,b,c = map(int, input().split())
    # 노드 u에서 v로 가는 비용이 w
    graph[a].append((b, c))


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
