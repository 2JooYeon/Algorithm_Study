n, m = map(int, input().split(" "))
hear = set()
sea = set()
for i in range(0, n) :
	hear.add(input())
for i in range(0, m) :
	sea.add(input())


ans = sorted(list(hear & sea))
print(len(ans))
for i in range(0, len(ans)) :
	print(ans[i])

