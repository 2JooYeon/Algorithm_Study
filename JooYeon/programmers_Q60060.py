def solution(words, queries):
    answer = []
    s_data = {}
    e_data = {}
    for word in words:
        len_w = len(word)
        for i in range(len_w):
            key = (word[:i], len_w)
            if key not in s_data:
                s_data[key] = 1
            else:
                s_data[key] += 1
            key = (word[i:], len_w)
            if key not in e_data:
                e_data[key] = 1
            else:
                e_data[key] += 1
    for q in queries:
        len_q = len(q)
        target = q.replace('?', '')
        if not len(target) and (target, len_q) in s_data:
            answer.append(s_data[(target, len_q)])
            continue
        if q[0] == '?':
            q = q.replace('?', '')
            if (q, len_q) in e_data:
                answer.append(e_data[(q, len_q)])
            else:
                answer.append(0)
        else:
            q = q.replace('?', '')
            if (q, len_q) in s_data:
                answer.append(s_data[(q, len_q)])
            else:
                answer.append(0)
            
    return answer
