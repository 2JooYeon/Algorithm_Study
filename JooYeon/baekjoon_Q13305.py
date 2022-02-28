import sys
input = sys.stdin.readline

answer = 0
n = int(input())
dist = list(map(int, input().split()))
money = list(map(int, input().split()))
for i in range(n):
    money[i] = [money[i], i]
money = money[:-1]
money.sort()

temp = n-1
for i in range(n-1):
    if money[i][1]<temp:
        answer += sum(dist[money[i][1]:temp])*money[i][0]
        temp = money[i][1]
print(answer)
