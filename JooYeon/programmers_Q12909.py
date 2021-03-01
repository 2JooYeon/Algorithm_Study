def solution(s):
    answer = True
    temp = []
    for element in s:
        if (element == '('):
            temp.append(element)
        elif (len(temp) and element == ')'):
            temp.pop()
        else:
            return False

    if (len(temp)):
        answer = False
    else:
        answer = True

    return answer