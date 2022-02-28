import sys
input = sys.stdin.readline

n = int(input())
count = 0
num = 666
while count<n:
    if '666' in str(num):
        count += 1
    num += 1
print(num-1)
