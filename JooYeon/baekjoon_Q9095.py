import sys
input = sys.stdin.readline

T = int(input())
n = []
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for _ in range(T):
    n.append(int(input()))

for num in range(4, 11):
    dp[num] += dp[num - 1]
    dp[num] += dp[num - 2]
    dp[num] += dp[num - 3]

for i in range(len(n)):
    print(dp[n[i]])
