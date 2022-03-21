target = int(input())
breakcnt = int(input())

if breakcnt > 0 :
	breaklst = list(map(int, input().split(' ')))
else :
	breaklst = []
    
answer = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)
    
    for j in range(len(nums)):
        if int(nums[j]) in breaklst:
            break

        elif j == len(nums) - 1:
            answer = min(answer, abs(int(nums) - target) + len(nums))

print(answer)