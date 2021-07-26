def solution(phone_number):
    n = len(phone_number)
    answer = ''
    for i in range(0,n-4):
        answer += '*'
    answer += phone_number[n-4]
    answer += phone_number[n-3]
    answer += phone_number[n-2]
    answer += phone_number[n-1]
    
    return answer