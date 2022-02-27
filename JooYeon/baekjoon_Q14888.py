import sys
import itertools
input = sys.stdin.readline

exp = ['+','-','*','//']
n = int(input())
numbers = list(map(int, input().split()))
num_exp = list(map(int, input().split()))
data = []
result = []
for i in range(4):
    data += [i]*num_exp[i]
per = itertools.permutations(data, n-1)
per = set(list(per))
for line in per:
    w = 0
    temp = numbers[w]
    for i in line:
        w += 1
        target= numbers[w]
        if i==0:
            temp = temp + target
        if i==1:
            temp = temp - target
        if i==2:
            temp = temp * target
        if i==3:
            if temp<0:
                temp = -temp
                temp = temp // target
                temp = -temp
            else:
                temp = temp // target
    result.append(temp)
print(max(result))
print(min(result))
