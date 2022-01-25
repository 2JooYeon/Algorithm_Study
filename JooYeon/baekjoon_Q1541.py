f = input().split('-')
num = []
for sub_f in f:
    n = 0
    temp = sub_f.split('+')
    for t in temp:
        n += int(t)
    num.append(n)
answer = num[0]
for data in num[1:]:
    answer -= data
print(answer)
