import sys
input = sys.stdin.readline

answer = []
n = int(input())
kg_h = []
for i in range(n):
    kg_h.append(list(map(int, input().split())) + [i])

kg_h.sort()
for i in range(n):
    temp = 0
    for kg, h, _ in kg_h[i:]:
        if kg_h[i][0]<kg and kg_h[i][1] < h:
            temp += 1
    answer.append([kg_h[i][2], temp+1])
answer.sort()
answer = list(map(lambda x:x[1], answer))
print(' '.join(map(str, answer)))
