import sys
input = sys.stdin.readline

n = int(input())
home = list(map(int, input().split()))
home.sort()
answer_odd = 0
answer_even_a = 0
answer_even_b = 0
if len(home)%2:
    print(home[len(home)//2])
else:
    a = (len(home)//2)-1
    b = len(home)//2
    for i in range(len(home)):
        if i == a:
            answer_even_b += abs(home[i]-home[b])
            continue
        if i == b:
            answer_even_a += abs(home[i]-home[a])
            continue
        answer_even_a += abs(home[i]-home[a])
        answer_even_b += abs(home[i]-home[b])
    if answer_even_a<=answer_even_b:
        print(home[a])
    else:
        print(home[b])
