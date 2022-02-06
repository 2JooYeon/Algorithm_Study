def solution(info, query):
    answer = []
    
    for q in query:
        q = q.replace('and', '').split()
        count = 0
        for n in info:
            satisfy = 1
            n = n.split()
            target = list(zip(q, n))
            for a, b in target[:-1]:
                if a == '-': continue
                if a!=b:
                    satisfy = 0
                    break
            if satisfy and int(target[-1][0])<=int(target[-1][1]):
                count += 1
        answer.append(count)
        
    return answer
