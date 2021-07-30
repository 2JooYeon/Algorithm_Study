N, M, K = map(int, input().split())
data = list(map(int, input().split()))

result = 0

while M > 0:
    for i in range(0,K):
        result += max(data)
        M -= 1
        if M==0:
            break
    if M==0:
            break
    md = max(data)
    data.remove(md)
    result += max(data)
    M -= 1
    data.append(md)

print(result)

# another method
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[N-1] # 가장 큰 수
second = data[N-2] # 두번째 큰 수

# 가장 큰 수가 더해지는 횟수
count = int(M / (K+1)) * K
count += M%(K+1)

result = 0
result += (count) * first
result += (M - count) * second
print(result)