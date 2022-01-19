def solution(n, k):
    answer = 0
    n_to_k = ''
    
    # 소수인지 판별하기 
    def isprime(num):
        for i in range(2, int(num**(0.5)+1)):
            if num % i == 0:
                return False
        return True
    
    # k진법으로 변환하기 
    while n > 0:
        n_to_k += str(n%k)
        n //= k
    n_to_k = n_to_k[::-1]
    
    # 0을 기준으로 숫자 분할하기 
    target = n_to_k.split('0')
    
    # 소수 개수 세기 
    for num in target:
        if num != '1' and num != '' and isprime(int(num)):
            answer += 1
    
    return answer
