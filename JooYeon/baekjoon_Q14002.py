import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
d = [1]*n
answer = []
for i in range(1, n):
    for j in range(0,i):
        if arr[j]<arr[i]:
            d[i] = max(d[i], d[j]+1)

max_len = max(d)
print(max_len)

for i in range(n-1, -1, -1):
    if d[i] == max_len:
        answer.append(arr[i])
        max_len -= 1
answer.reverse()
print(' '.join(map(str, answer)))
