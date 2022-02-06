from bisect import bisect_left, bisect_right
def solution(words, queries):
    answer = []
    
    def count_by_range(data, left, right):
        l_index = bisect_left(data, left)
        r_index = bisect_right(data, right)
        return r_index - l_index
    
    data = {}
    r_data = {}
    for word in words:
        len_w = len(word)
        if len_w not in data:
            data[len_w] = [word]
            r_data[len_w] = [word[::-1]]
        else:
            data[len_w].append(word)
            r_data[len_w].append(word[::-1])
            
    for key in data:
        data[key].sort()
        r_data[key].sort()
        
    for q in queries:
        len_q = len(q)
        if q[0] != '?':
            left = q.replace('?', 'a')
            right = q.replace('?', 'z')
            if len_q in data:
                answer.append(count_by_range(data[len_q], left, right))
            else:
                answer.append(0)
        else:
            left = q.replace('?', 'a')[::-1]
            right = q.replace('?', 'z')[::-1]
            if len_q in r_data:
                answer.append(count_by_range(r_data[len_q], left, right))
            else:
                answer.append(0)
    
    return answer
