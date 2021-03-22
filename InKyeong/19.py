import math
def solution(name):
    answer = 0
    answer1 = 0
    answer2 = 0
    inputname = []
    for i in name :
        inputname.append(ord(i))
    for i in inputname:
        if i<=78 :
            answer1 += (i-64)
        else :
            answer1 += (92-i)
    answer1 -= 1
    maxa = math.ceil(len(inputname)/2)
    i = 0
    answer2 = 0
    for j in inputname :
        if i<maxa and inputname[i] == 65 and inputname[i+1] == 65 :
            p = i
            while inputname[i] == 65 :
                inputname[i] = 0
                i += 1
            k = 0
            for k in range(len(inputname)) :
                if inputname[k]==0:
                    print(answer2)
                elif inputname[k]<=78 and inputname[k] != 0 :
                    answer2 += (inputname[k]-64)
                    print(answer2)
                elif inputname[k]>78 and inputname[k] != 0 :
                    answer2 += (92-inputname[k])
                    print(answer2)   
            answer = answer2+p-2
            break
        elif i==1 and inputname[i] == 65 :
            answer = answer1 - 1
            break
        else :
            i += 1
            answer = answer1
    return answer

