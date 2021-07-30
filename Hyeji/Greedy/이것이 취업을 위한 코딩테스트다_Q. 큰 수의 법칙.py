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

