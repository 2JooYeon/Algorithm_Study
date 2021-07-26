def solution(n):
    answer = ''
    a = '수'
    b = '박'
 
    for i in range(0,n) :
        if (i%2==1) :
            answer += b
        else :
            answer += a
  
    return answer