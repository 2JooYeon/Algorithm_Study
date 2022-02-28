import sys
from collections import defaultdict
input = sys.stdin.readline

n = input().rstrip()
start = int(n)-9*(len(n)-1)-int(n[0])
n = int(n)
data = defaultdict(list)
for i in range(start, n+1):
    temp = i + sum(map(int, list(str(i))))
    data[temp].append(i)
if n in data:
    print(data[n][0])
else:
    print(0)
