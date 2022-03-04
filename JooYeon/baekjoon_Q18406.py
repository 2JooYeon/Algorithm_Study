import sys
input = sys.stdin.readline

num = list(map(int, list(input().rstrip())))
n = len(num)//2
if sum(num[:n]) == sum(num[n:]):
    print('LUCKY')
else:
    print('READY')
