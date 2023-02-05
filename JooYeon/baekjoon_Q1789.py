import sys
input = sys.stdin.readline

s = int(input())
temp = 0
n = 1
while temp<=s:
    temp+=n
    n+=1

print(n-2)