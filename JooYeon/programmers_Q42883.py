def solution(number, k):
    answer = ''
    select = len(number) - k
    index = 0

    while 1:
        target = max(number[index:len(number) - select + 1])
        answer += target
        index = number[index:len(number) - select + 1].find(target) + 1 + index
        select -= 1
        if index == len(number) - select:
            answer += number[index:]
            return answer
        elif select == 0:
            return answer
