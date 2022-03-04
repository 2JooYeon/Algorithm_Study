import sys
input = sys.stdin.readline

s = list(input().rstrip())
char = []
num = []
for c in s:
    if c.isalpha():
        char.append(c)
    else:
        num.append(int(c))
char.sort()
num = sum(num)
print(''.join(char)+str(num))
