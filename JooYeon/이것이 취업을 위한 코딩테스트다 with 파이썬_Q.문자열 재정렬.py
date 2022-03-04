import sys
input = sys.stdin.readline

s = list(input().rstrip())
char = []
num = 0
for c in s:
    if c.isalpha():
        char.append(c)
    else:
        num+=int(c)
char.sort()
if num:
    print(''.join(char)+str(num))
else:
    print(''.join(char))
