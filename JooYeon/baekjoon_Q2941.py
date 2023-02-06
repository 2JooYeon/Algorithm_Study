import sys
input = sys.stdin.readline

word = input().rstrip()
alpha_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for alpha in alpha_list:
    word = word.replace(alpha, '.')

print(len(word))