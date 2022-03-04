import sys
input = sys.stdin.readline

line = list(input())
reverse_zero = 0
reverse_one = 0
flag_zero= 1
flag_one = 1
for i in range(len(line)):
    if line[i] == '0':
        flag_one = 1
        if flag_zero:
            reverse_zero += 1
            flag_zero = 0
    if line[i] == '1':
        flag_zero = 1
        if flag_one:
            reverse_one += 1
            flag_one = 0

print(min(reverse_one, reverse_zero))
