import sys
input = sys.stdin.readline

n = int(input())
line = []
for _ in range(n):
    line.append(list(map(int, input().split())))
line.sort()
start = line[0][0]
end = line[0][1]
answer = end-start
for a, b in line[1:]:
    if end<a:
        start = a
    else:
        start = end
    if end<b:
        end = b
    answer += end-start
print(answer)
