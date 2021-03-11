import heapq

def solution(scoville, K):
    answer = 0
    data = []
    for value in scoville:
        heapq.heappush(data,value)

    while 1:
        first = heapq.heappop(data)
        if len(data) and first >= K:
            return answer
        elif len(data) and first < K:
            second = heapq.heappop(data)
            heapq.heappush(data, first + second*2)
            answer += 1
        else:
            return (answer if first >= K else -1)
    return answer