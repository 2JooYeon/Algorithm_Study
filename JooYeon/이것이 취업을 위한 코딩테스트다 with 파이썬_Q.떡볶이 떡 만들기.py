import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rice = list(map(int, input().split()))

start = 0
end = max(rice)

result = 0
while (start<=end):
    total = 0
    mid = (start+end)//2
    for x in rice:
        if x>mid:
            total+=x-mid
    if total<m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
