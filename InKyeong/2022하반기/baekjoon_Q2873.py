import sys
# 초기값
x, y = map(int, sys.stdin.readline().split(" "))
arr = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(0, x)]
answer1 = ""

r1 = ""
l1 = ""
d1 = ""
u1 = ""
for _ in range(1, y) :
	r1 += "R"
	l1 += "L"
for _ in range(1, x) :
	d1 += "D"
	u1 += "U"

answer = ""
pair = ""
if x % 2 == 1 :
	# 무조건 오른쪽으로 출발 + 전체 다 더하면 됨
	answer += r1
	pair += "D" + l1 + "D" + r1
	answer += pair * (x // 2)
	print(answer)
  
elif x % 2 == 0 and y % 2 == 1 :
	# 무조건 아래쪽으로 출발 + 전체 다 더하면 됨
	answer += d1
	pair += "R" + u1 + "R" + d1
	answer += pair * (y // 2)
	print(answer)

else :
	remainver = 0
	remainhor = 0
	for i in range(0, x-1) :
		remainhor += arr[i][y-1]
	for i in range(0, y-1) :
		remainver += arr[x-1][i]
	if remainhor >= remainver :
		# 오른쪽 출발
		answer += r1 + "D"
		pair += l1 + "D" + r1 + "D"
		answer += pair * (x // 2 - 1)
		print(answer)
	else :
		# 아래쪽 출발
		answer += d1 + "R"
		pair += u1 + "R" + d1 + "R"
		answer += pair * (y // 2 - 1)
		print(answer)
