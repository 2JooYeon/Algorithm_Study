import sys

N, K = map(int, input().split())
coin = []
count = 0

for i in range(0, N):
    coin.append(int(sys.stdin.readline().rstrip()))

while K > 0:
    target = coin.pop()
    count += K // target
    K %= target

print(count)