
minuslst = []
minuslen = 0
pluslst = []
pluslen = 0
lstlen = int(input())
answer = 0

for _ in range(lstlen):
	inputlen = int(input())
	if (inputlen <= 0) :
		minuslst.append(inputlen)
		minuslen += 1
	else :
		if (inputlen == 1) :
			answer += 1
			continue
		pluslst.append(inputlen)
		pluslen += 1

minuslst.sort()
pluslst.sort(reverse=True)

if pluslen % 2 == 0:
    for i in range(0, pluslen, 2):
        answer += pluslst[i] * pluslst[i+1]
else:
    for i in range(0, pluslen - 1, 2):
        answer += pluslst[i] * pluslst[i+1]
    answer += pluslst[pluslen - 1]

if minuslen % 2 == 0:
    for i in range(0, minuslen, 2):
        answer += minuslst[i] * minuslst[i+1]
else:
    for i in range(0, minuslen - 1, 2):
        answer += minuslst[i] * minuslst[i+1]
    answer += minuslst[minuslen - 1]

print(answer)