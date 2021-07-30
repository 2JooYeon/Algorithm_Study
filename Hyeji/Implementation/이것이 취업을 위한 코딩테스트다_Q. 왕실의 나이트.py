data = input()
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1

step = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
result = 0

for s in step:
    nr = row + s[0]
    nc = row + s[1]
    if nr < 1 or nr >8 or nc < 1 or nc >8:
        continue
    result += 1
print(result)