from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    data = {}
    for n in info:
        n = n.split()
        target = n[:-1]
        score = int(n[-1])
        for i in range(5):
            for c in combinations(target, i):
                key = ''.join(c)
                if key in data:
                    data[key].append(score)
                else:
                    data[key] = [score]
    for key in data:
        data[key].sort()
        
    for q in query:
        q = q.replace('and', '').replace('-', '').split()
        cond = q[:-1]
        cond_s = ''.join(cond)
        cut = int(q[-1])
        if cond_s in data:
            index = bisect_left(data[cond_s], cut)
            answer.append(len(data[cond_s])-index)
        else:
            answer.append(0)
    
    return answer
