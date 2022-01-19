from itertools import combinations

def solution(nums):
    answer = 0
    
    def isprime(n):
        for i in range(2, int(n**(0.5)+1)):
            if n%i ==0:
                return False
        return True
    
    targets = combinations(nums, 3)
    
    for target in targets:
        if isprime(sum(target)):
            answer += 1
            
    return answer
