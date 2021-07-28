
n, m = map(int, input().split())

tree = list(map(int, input().split()))

tree.sort()


def branch(target) :
    branch = 0
    for i in range(0, n):
        if tree[i] <= target :
            continue
        elif tree[i] > target :
            branch += (tree[i] - target)

    return branch

target = tree[n-1]

while 1 :
    if branch(target) < m :
        target -= 1
    elif branch(target) >=m :
        print(target)
        break