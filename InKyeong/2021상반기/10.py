import heapq
from collections import deque

def sorting(num) :
    h = []
    result = []
    for i in num :
        heapq.heappush(h, i)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

def solution(operations) :
    answer = [0,0]
    num = []
    for i in operations :
        if ("I" in i) :
            strnum = i.split()
            num.append(int(strnum[1]))
            num.sort()
            print(">>>", num)
        elif ("D 1" == i) :
            data = deque(num)
            if len(data) == 0 :
                break
            data.pop()
            num = []
            for i in range(len(data)):
                num.append(data[i])
            print("1", num)
            
        elif ("D -1" == i) :
            data = deque(num)
            if len(data) == 0 :
                break
            else :
                data.popleft()
            num = []
            for i in range(len(data)):
                num.append(data[i])
            print("-1", num)
            
    
    if len(num) == 0 :
        answer = [0,0]
    else :
        copy = deque(num)
        answer[0] = copy.pop()
        answer[1] = copy.popleft()
    return answer