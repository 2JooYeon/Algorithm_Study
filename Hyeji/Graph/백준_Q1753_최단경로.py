import sys
import heapq

INF = int(1e9)

vertex = [[] for i in range(20001)]
distance = [[INF] * (20001) for i in range(20001)]
# v는 정점의 개수, e는 간선의 개수
v, e = input().split()
v = int(v)
e = int(e)
# k는 시작 정점의 번호
k = int(input())

for _ in range(0,e):
    a,b,c = map(int, sys.stdin.readline().split())
    vertex[a].append((b,c))

q = []
heapq.heappush(q,(0,k))
distance[k][k] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[k][now] < dist:
        continue
    for i in vertex[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
for i in range(1, v+1):
    print(distance[i])
