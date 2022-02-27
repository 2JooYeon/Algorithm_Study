import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = []
def dfs(start):
    if len(seq) == m:
        print(' '.join(map(str, list(seq))))
        return
    for i in range(start, n+1):
        seq.append(i)
        dfs(i)
        seq.pop()
dfs(1)
