from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    comb_data = []
    
    for num in course:
        for order in orders:
            order = sorted(order)
            comb_data += combinations(order, num)
            counter = Counter(comb_data)
        if len(counter):
            max_count = max(list(counter.values()))
            if max_count >=2:
                for k, v in counter.items():
                    if v == max_count:
                        answer.append(''.join(k))
        comb_data = []
    answer.sort()
    return answer
