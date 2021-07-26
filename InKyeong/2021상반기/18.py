
N, M, K = map(int, input().split())
num = list(map(int, input().split()))
num.sort(reverse=True)

num1 = num[0]
num2 = num[1]
answer = 0
count = 0
for i in range(0, M) :
    if count < K :
        answer += num1
        count += 1
    else : 
        answer += num2
        count = 0

print(answer)


