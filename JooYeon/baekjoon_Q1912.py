import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
d = [-1001]*n
d[0] = arr[0]
for i in range(1,n):
    d[i] = max(d[i-1]+arr[i], arr[i])
print(max(d))
