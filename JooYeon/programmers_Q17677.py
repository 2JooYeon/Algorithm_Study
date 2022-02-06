def solution(str1, str2):
    answer = 0
    data1 = []
    data2 = []
    union = 0
    inter = 0
    
    for i in range(len(str1)-1):
        target = str1[i:i+2]
        if target.isalpha():
            data1.append(target.lower())
    for i in range(len(str2)-1):
        target = str2[i:i+2]
        if target.isalpha():
            data2.append(target.lower())
            
    for word in data1[:]:
        if word in data2[:]:
            inter += 1
            data1.remove(word)
            data2.remove(word)

    union = inter + len(data1) + len(data2)
    if union:
        answer = int(65536*(inter/union))
    else:
        answer = 65536
        
    return answer
