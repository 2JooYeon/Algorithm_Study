import heapq
from collections import deque

def solution(jobs):
    sorted_time = []
    # 정렬 첫 번째 기준 : 작업 소요시간 / 두 번째 기준 : 작업 요청 시
    jobs.sort(key=lambda x: (x[0], x[1]))
    data = deque(jobs)
    work_num = len(jobs)

    # 가장 먼저 들어온 요청 처리하기
    temp = data.popleft()
    current = temp[0] + temp[1]
    all_time = temp[1]

    # 작업 소요시간 기준으로 최소힙 만들기
    for value in data:
        heapq.heappush(sorted_time, (value[1], value[0]))

    while len(sorted_time):
        work_time = heapq.heappop(sorted_time)
        # 작업 소요시간 제일 작은요소의 작업 요청 시점이 과거일때
        if work_time[1] <= current:
            data.remove(list((work_time[1], work_time[0])))
            current += work_time[0]
            all_time += (current - work_time[1])
        # 작업 소요시간 제일 작은요소의 작업 요청 시점이 미래일때
        else:
            # 가장 먼저 요청이 들어온 작업 처리하기
            temp = data.popleft()
            # 작업이 종료된 시점보다 요청 시점이 과거일때
            if temp[0] <= current:
                data.appendleft(temp)
                # 작업이 종료된 시점보다 요청 시점이 과거인 요소들 중에 소요시간이 가장 적은 작업 고르기
                test = list(filter(lambda x: x[0] <= current, data))
                test.sort(key=lambda x: x[1])
                current += test[0][1]
                all_time += (current - test[0][0])
                data.remove([test[0][0], test[0][1]])
                # 최소힙 재정렬하기
                sorted_time.clear()
                for value in data:
                    heapq.heappush(sorted_time, (value[1], value[0]))
            # 작업이 종료된 시점보다 요청 시점이 미래일때
            else:
                current = temp[0] + temp[1]
                all_time += temp[1]

    return all_time // work_num

# print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
# print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
# print(solution([[0, 3], [1, 9], [2, 6]]), 9)
# print(solution([[0, 1]]), 1)
# print(solution([[1000, 1000]]), 1000)
# print(solution([[0, 1], [0, 1], [0, 1]]), 2)
# print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
# print(solution([[0, 1], [1000, 1000]]), 500)
# print(solution([[100, 100], [1000, 1000]]), 500)
# print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
# print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)
# print(solution([[0,1],[0,1],[1,0]]),1)