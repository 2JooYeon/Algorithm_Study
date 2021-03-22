import math
def solution(answers):
    answer = []
    num = len(answers)
    one = 0
    two = 0
    three = 0
    first = [1, 2, 3, 4, 5] * math.ceil(num/5)
    second = [2, 1, 2, 3, 2, 4, 2, 5] * math.ceil(num/8)
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * math.ceil(num/10)
    for i in range(num) :
        if first[i] == answers[i] : one += 1
        if second[i] == answers[i] : two += 1
        if third[i] == answers[i] : three += 1
    maxnum = max(one, two, three) 
    if maxnum == one : answer.append(1)
    if maxnum == two : answer.append(2)
    if maxnum == three : answer.append(3)
    return answer