def solution(s):
    answer = len(s)
    count = 0
    answer_s = ""
    i = 0
     
    for n in range(1, len(s)//2+1):
        splited = []
        count = 1
        answer_s = ''
        target = s[0:n]
        for i in range(n, len(s)+1, n):
            if target == s[i:i+n]:
                count += 1
            else:
                if count == 1:
                    answer_s += target
                else:
                    answer_s += str(count)+target
                target = s[i:i+n]
                count = 1
        answer_s += s[i:]
        if answer > len(answer_s):
            answer = len(answer_s)


    return answer
