N = int(input())

count = 0
while N > 2 :
	if N % 5 == 0 :
		count += (N // 5)
		N = 0
	else :
		count += 1
		N = N - 3

if N == 0 :
	print(count)
else :
	print(-1)


