N = int(input())

K = list(map(int, input().split()))

d = [0] * 100

d[0] = K[0]
d[1] = max(K[0], K[1])
for i in range(2, N):
    d[i] = max(d[i-2] + K[i], d[i-1])

print(d[N-1])