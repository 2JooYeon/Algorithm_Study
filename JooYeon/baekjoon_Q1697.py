from collections import deque

n, k = map(int, input().split())
limit = 100000
visited_sec =[0]*(limit+1)
queue = deque([n])

while queue:
    cur = queue.popleft()
    if cur == k:
        print(visited_sec[cur])
        break
    for w in [cur-1, cur+1, cur*2]:
        if 0<=w<=limit and not visited_sec[w]:
            visited_sec[w] = visited_sec[cur]+1
            queue.append(w)
