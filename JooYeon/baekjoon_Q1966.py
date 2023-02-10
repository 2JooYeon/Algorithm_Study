import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, i = map(int, input().split())
    priority = deque(map(int, input().split()))
    index_prior = deque(enumerate(priority))
    count = 1
    while index_prior:
        # 우선순위가 가장 높으면
        idx, prior = index_prior.popleft()
        if prior == max(priority):
            # 찾고자 하는 문서면
            if idx == i:
                print(count)
                break
            # 찾고자 하는 문서가 아니면
            priority.popleft()
            count += 1
        # 우선순위가 가장 높지 않으면
        else:
            priority.popleft()
            priority.append(prior)
            index_prior.append((idx, prior))