import sys
from bisect import bisect_left, bisect_right

answer = 0
input = sys.stdin.readline
n, m = map(int, input().split())
s = []
len_s = 0
target = []

for i in range(n):
    word = input().rstrip()
    len_s = max(len_s, len(word))
    s.append(word)

s.sort()

for i in range(m):
    word = input().rstrip()
    plus_c = len_s - len(word)
    left = word + ('a' * plus_c)
    right = word + ('z' * plus_c)
    target.append((left, right))

for word in target:
    left = bisect_left(s, word[0])
    right = bisect_right(s, word[1])
    if left != right:
        answer += 1
    else:
        if word in s:
            answer += 1

print(answer)
