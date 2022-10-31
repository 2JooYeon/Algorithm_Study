import itertools

N, C = map(int, input().split(" "))
data = []
for i in range(0, N) :
	data.append(int(input()))

data.sort()

combi = []
for i in itertools.combinations(data, C) :
	combi.append(i)


_maxnum = 0

for i in combi :
	minnum = 1000000000
	for j in range(1, C) :
		minus = i[j] - i[j-1]
		if minnum > minus :
			minnum = minus
	if minnum > _maxnum :
		_maxnum = minnum

print(_maxnum)