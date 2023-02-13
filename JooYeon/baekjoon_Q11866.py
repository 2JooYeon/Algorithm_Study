import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque(range(1, n+1))
answer = []
while q:
    for _ in range(k-1):
        temp = q.popleft()
        q.append(temp)
    data = q.popleft()
    answer.append(str(data))

print('<', end='')
for i in answer[:-1]:
    print(i+', ', end='')
print(answer[-1]+'>')


