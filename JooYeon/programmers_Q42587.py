from collections import deque

def solution(priorities, location):
    answer = 0
    is_printed = False
    data = deque([(v, i) for i, v in enumerate(priorities)])

    while 1:
        target = data.popleft()
        if len(data) and target[0] >= max(data)[0]:
            answer += 1
            if location == target[1]:
                return answer
        elif len(data) and target[0] < max(data)[0]:
            data.append(target)
        else:
            return answer + 1


# 런타임 발생 에러 코드
# def solution(priorities, location):
#     answer = 0
#     data = deque([(v, i) for i, v in enumerate(priorities)])
#
#     while (1):
#         target = data.popleft()
#         if target[0] >= max(data)[0]:
#             answer += 1
#             if location == target[1]:
#                 return answer
#         else:
#             data.append(target)

