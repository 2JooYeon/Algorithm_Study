from collections import deque

def solution(progresses, speeds):
    answer = []
    deploy = []
    lennum = len(speeds)
    for i in range(lennum) :
        if ((100 - progresses[i]) % speeds[i]) == 0 :
            num = (int)((100 - progresses[i]) / speeds[i] )
        else :
            num = (int)((100 - progresses[i]) / speeds[i] + 1 )
        deploy.append(num)
    
    front = 0   
    
    for idx in range(len(deploy)):
        if deploy[idx] > deploy[front]:  
            answer.append(idx - front)
            front = idx 
            
    answer.append(len(deploy) - front) 
    
    return answer