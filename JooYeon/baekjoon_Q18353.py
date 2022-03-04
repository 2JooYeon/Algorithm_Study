import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
s.reverse()
final = [s[0]]
answer = 0
for i in range(1,n):
    if final[-1]<s[i]:
        final.append(s[i])
    else:
        answer += 1
        left = bisect_left(final, s[i])
        final[left] = s[i]
print(answer)
