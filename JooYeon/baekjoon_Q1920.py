import sys
n = int(input())
data = set(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
for n in numbers:
    if n in data:
        print(1)
    else:
        print(0)
