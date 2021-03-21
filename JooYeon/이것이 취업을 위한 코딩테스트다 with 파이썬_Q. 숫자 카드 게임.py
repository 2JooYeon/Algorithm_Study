N, M = map(int, input().split())
data = []
min_value = []

for i in range(0, N):
    data.append(list(map(int, input().split())))

for value in data:
    min_value.append(min(value))

min_value.sort(reverse=True)

print(min_value[0])