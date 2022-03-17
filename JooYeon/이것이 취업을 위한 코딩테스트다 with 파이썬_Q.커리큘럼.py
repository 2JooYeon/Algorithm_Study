import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input().rstrip())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
class_time = {}
answer = {}
for i in range(1, n+1):
    data = list(map(int, input().split()))
    class_time[i] = data[0]
    answer[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    queue = deque([])
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            indegree[i] -= 1
            answer[i] = max(answer[i], answer[cur]+class_time[i])
            if indegree[i] == 0:
                queue.append(i)

topology_sort()
for i in range(1, n+1):
    print(answer[i])
