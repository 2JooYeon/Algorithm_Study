# from collections import deque
# def solution(jobs):
#     answer = 0
#     jobs = sorted(jobs, key = lambda x : x[1])
#     jobs = deque(jobs)
#     now = 0
#     lennum = len(jobs)
#     while len(jobs) > 0 :
#         i = 0
#         if jobs[i][0] <= now :
#             now += jobs[i][1]
#             answer += now - jobs[i][0]
#             jobs.popleft()
#         else :
#             i += 1
#     answer = answer / lennum
#     return answer
# 시간 초과 및 테스트케이스 고려 X


import heapq

def solution(jobs):
    count, last, answer = 0, -1, 0
    heap = []
    jobs.sort()
    time = jobs[0][0]
    while count < len(jobs):
        for s, t in jobs:
            if last < s <= time:
                heapq.heappush(heap, (t, s))
        if len(heap) > 0:
            count += 1
            last = time
            term, start = heapq.heappop(heap)
            time += term
            answer += (time - start)
        else:
            time += 1
    return answer//len(jobs)