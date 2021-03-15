from collections import deque
def solution(priorities, location):
    answer = 0
    
    d = deque([(v,i) for i,v in enumerate(priorities)])
    first = max(d)
    while len(d)!=0:
        if d[0][0] != first[0]:
            a = d.popleft()
            d.append(a)
        else :
            if d[0][1] == location :
                answer += 1
                break
            else :
                d.popleft()
                if len(d) == 0 :
                    answer += 1
                    break
                else :
                    first = max(d)
                    answer += 1
    return answer