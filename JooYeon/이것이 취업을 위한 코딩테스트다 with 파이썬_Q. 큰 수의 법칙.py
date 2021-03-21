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