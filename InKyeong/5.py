def solution(clothes):
    answer = 1
    
    data = dict()
    array = []
    for i in range(len(clothes)) :
        
        data[clothes[i][1]] = None
        array.append(clothes[i][1])
        
    for i in array :
        data[i] = array.count(i)
    
    for i in data.values() :
        answer *= (i+1)
        
    return answer-1


###################################################
# import collections
# from functools import reduce

# def solution(clothes):
#     return reduce(lambda x, y : x*y,a+1 for a in collections.Counter([x[1] for x in clothes] )] )
# reduce 로 [] 안에 값 다 반복
# collections로 같은 종류의 옷 숫자 세주기