import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr_reverse = arr[::-1]
increase_d = [1]*n
decrease_d = [1]*n

for i in range(n):
    for j in range(i):
        if arr[j]<arr[i]:
            increase_d[i] = max(increase_d[j] + 1, increase_d[i])
        if arr_reverse[j]<arr_reverse[i]:
            decrease_d[i] = max(decrease_d[j]+1, decrease_d[i])
answer = [0]*n
decrease_d.reverse()
for i in range(n):
    answer[i] = increase_d[i]+decrease_d[i]-1
print(max(answer))
