def solution(N, stages):
    answer = []
    for n in range(1, N+1):
        clear = len(list(filter(lambda x:x>=n, stages)))
        if clear == 0:
            ratio = 0
        else:
            fail = stages.count(n) 
            ratio = fail/clear
        answer.append([ratio, n])
    answer.sort(key = lambda x: (x[0], -x[1]), reverse = True)
    answer = list(map(lambda x:x[1], answer))
    return answer
