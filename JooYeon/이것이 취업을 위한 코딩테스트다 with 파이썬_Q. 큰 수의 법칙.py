N, M, K = map(int, input().split())

num = list(map(int, input().split()))
num.sort(reverse=True)

first = num[0]
second = num[1]

answer = 0
limit = 0

for i in range(0, M):
    if limit == K:
        answer += second
        limit = 0
        continue
    limit += 1
    answer += first

print(answer)

N, M, K = map(int, input().split())
num = list(map(int, input().split()))

num.sort(reverse=True)

first = num[0]
second = num[1]

# 가장 큰 수가 더해지는 횟수 구하기
count = int(M/(K+1)) * K
count += M % (K+1)

answer = 0
answer += count * first # 가장 큰 수 더하기
answer += (M - count) * second # 두 번째로 큰 수 더하기

print(answer)