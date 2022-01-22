def solution(s, n):
    answer = ''
    for c in s:
        if c.islower():
            if ord(c)+n>122:
                answer+=chr(97+ord(c)+n-122-1)
            else:
                answer+=chr(ord(c)+n)
        elif c.isupper():
            if ord(c)+n>90:
                answer+=chr(65+ord(c)+n-90-1)
            else:
                answer+=chr(ord(c)+n)
        else:
            answer += ' '
    return answer
