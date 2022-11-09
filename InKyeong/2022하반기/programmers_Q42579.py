def solution(genres, plays):
    answer = []
    check = list(set(genres))
    d = dict()
    for i in range(0, len(check)) :
        d[check[i]] = [0, {}, []]

    for i in range(0, len(plays)) :
        d[genres[i]][0] += plays[i]
        d[genres[i]][1][i] = plays[i]
        d[genres[i]][2].append(plays[i])
        d[genres[i]][2].sort(reverse=True)
    
    value = list(d.values())
    value.sort(key = lambda x : x[0], reverse = True)
    
    for i in range(0, len(value)) :
        if len(value[i][2]) >= 2 :
            check = [k for k, v in value[i][1].items() if v == value[i][2][0]]
            if len(check) >= 2 :
                while len(check) != 2 :
                    check.pop()
                answer += check
            else :
                answer += check
                answer += [k for k, v in value[i][1].items() if v == value[i][2][1]]
        else :
            answer += list(value[i][1].keys())
    return answer