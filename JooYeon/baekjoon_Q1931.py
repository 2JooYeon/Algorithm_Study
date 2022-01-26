import sys

n = int(input())
c = []
for i in range(n):
    s, e = list(map(int, sys.stdin.readline().rstrip().split()))
    c.append([s,e])
c.sort(key=lambda x:(x[1], x[0]))

ex_e = c[0][1]
answer = 1
for data in c[1:]:
    cur_s, cur_e = data[0], data[1]
    if cur_s>=ex_e:
        answer += 1
        ex_e = cur_e

print(answer)
