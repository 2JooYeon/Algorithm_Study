n, m = map(int, input().split(' '))

if (n == 1) :
	answer = 1
elif (n == 2) :
	if ((m + 1) // 2 < 4) :
		answer = (m + 1) // 2
	else :
		answer = 4
else :
	if (m < 7) :
		answer = min(4, m)
	else :
		answer = m - 2

print(answer)