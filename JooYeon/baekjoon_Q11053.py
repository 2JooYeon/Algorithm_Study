import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

d = [arr[0]]
for num in arr[1:]:
    if num<d[-1]:
        left = bisect_left(d, num)
        d[left] = num
    elif num>d[-1]:
        d.append(num)
print(len(d))
