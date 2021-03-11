import heapq


def solution(operations):
    answer = []
    data = []

    for operation in operations:

        if operation[0] == "I":
            heapq.heappush(data, int(operation[2:]))
        else:
            if len(data) and operation[2] == '1':
                temp = []
                for value in data:
                    heapq.heappush(temp, -value)
                heapq.heappop(temp)
                data.clear()
                for value in temp:
                    heapq.heappush(data, -value)

            elif len(data) and operation[2] == '-':
                heapq.heappop(data)


    if len(data):
        temp = []
        for value in data:
            heapq.heappush(temp, -value)
        max = heapq.heappop(temp)
        answer.append(-max)
        answer.append(heapq.heappop(data))

    else:
        answer = [0, 0]

    return answer
