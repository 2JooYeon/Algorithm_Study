
M = int(input())

step = []
dp = [0 for _ in range(0, M)]

for _ in range(0, M) :
	step.append(int(input()))

for i in range(0, M) :
	if i == 0 :
		dp[0] = step[0]
	elif i == 1 :
		dp[1] = step[0] + step[1]
	elif i == 2 :
		dp[2] = max(step[0], step[1]) + step[2]
	else :
		dp[i] = max(dp[i-3] + step[i-1] + step[i], dp[i-2] + step[i])
	
print(dp[M-1])
