n = int(input())
temp = 0
line = 1
reverse = 0

# 대각선 몇 번째 줄인지 찾기
while n - temp > 0:
    temp += line
    line += 1

line -= 1
temp = 0

# 라인이 짝수면 거꾸로 시작
if line % 2 == 0:
    reverse = 1
# 라인이 홀수면 그대로 시작

# 대각선 라인에서 몇 번째 분수인지 찾기
for i in range(1, line):
    temp += i


if reverse:
    where_index = line - (n-temp)
else:
    where_index = n - temp - 1


# 분자
a = line-where_index
# 분모
b = 1 + where_index

print(f"{a}/{b}")