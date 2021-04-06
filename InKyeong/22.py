def solution(n, lost, reserve):
    reserve.sort() 
    for i in reserve: 
        if i in lost: 
            lost.remove(i) 
            reserve[reserve.index(i)] = -5 
            
    for i in reserve: 
        if i-1 in lost: 
            lost.remove(i-1) 
        elif i+1 in lost: 
            lost.remove(i+1) 
    return n-len(lost)

      