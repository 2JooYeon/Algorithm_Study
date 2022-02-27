import sys
input = sys.stdin.readline

n = int(input())
count = 0
seq = []

def is_diagonal(x):
    index = 0
    len_x = len(seq)
    for num in seq:
        if abs(x-num) == abs(len_x-index):
            return False
        index += 1
    return True

def bt():
    global count
    if len(seq)==n:
        count += 1
        return
    for i in range(n):
        if i not in seq:
            if not len(seq) or is_diagonal(i):
                seq.append(i)
                bt()
                seq.pop()
bt()
print(count)
