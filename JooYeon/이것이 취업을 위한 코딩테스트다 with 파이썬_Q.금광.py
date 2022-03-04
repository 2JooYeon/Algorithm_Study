import sys
input = sys.stdin.readline

t = int(input())
answer = []

def make_dp(d, gold, n, m):
    answer  = 0
    for i in range(n):
        d[i][0] = gold[i][0]
    for i in range(1, m):
        for j in range(n):
            if j-1<0 and j+1>=n:
                target = d[j][i-1]
            elif j-1<0:
                target = max(d[j][i-1], d[j+1][i-1])
            elif j+1>=n:
                target = max(d[j][i - 1], d[j - 1][i - 1])
            else:
                target = max(d[j][i - 1], d[j - 1][i - 1], d[j+1][i-1])
            d[j][i] = target + gold[j][i]
    for i in range(n):
        answer = max(answer, d[i][m-1])
    return answer

for _ in range(t):
    n,m = map(int, input().split())
    gold = []
    d = [[0 for _ in range(m)] for _ in range(n)]
    data = list(map(int, input().split()))
    for i in range(0, len(data), m):
        gold.append(data[i:i+m])
    answer.append(make_dp(d, gold, n, m))

for a in answer:
    print(a)
