import math


def solution(progresses, speeds):
    answer = []

    work_days = list(map(lambda x, y: math.ceil((100 - x) / speeds[y]), progresses, range(len(speeds))))

    target = work_days[0]
    count = 1
    for i in range(1, len(work_days)):
        if work_days[i] <= target:
            count += 1
        elif work_days[i] > target:
            answer.append(count)
            target = work_days[i]
            count = 1
        if i == (len(work_days) - 1):
            answer.append(count)

    return answer