def solution(n):
    answer = ''
    while n > 0:
        if n % 3:
            answer += str(n%3)
            n //= 3
        else:
            answer += '4'
            n //= 3
            n -= 1
    answer = answer[::-1]
    return answer
