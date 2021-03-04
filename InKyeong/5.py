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