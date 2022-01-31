def solution(left, right):
    answer = 0
        
    for n in range(left, right+1):
        if n**0.5 - int(n**0.5) == 0:
            answer -= n
        else:
            answer += n
    
    return answer
