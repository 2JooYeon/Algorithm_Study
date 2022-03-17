import sys
from collections import deque
input = sys.stdin.readline


def topology_sort(indegree, graph, answer, build_time):
    queue = deque([])
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            indegree[i] -= 1
            answer[i] = max(answer[i], answer[cur] + build_time[i])
            if indegree[i] == 0:
                queue.append(i)


t = int(input().rstrip())
result = []
for _ in range(t):
    n, k = map(int, input().split())
    indegree = [0] * (n+1)
    build_time = {}
    answer = {}
    graph = [[] for _ in range(n+1)]
    times = list(map(int, input().split()))
    for i in range(1, n+1):
        build_time[i] = times[i-1]
        answer[i] = times[i-1]
    for i in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    topology_sort(indegree, graph, answer, build_time)
    w = int(input().rstrip())
    result.append(answer[w])

for r in result:
    print(r)
