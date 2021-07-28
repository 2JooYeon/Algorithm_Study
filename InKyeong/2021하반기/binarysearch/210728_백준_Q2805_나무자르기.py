n, m = map(int, input().split())

tree = list(map(int, input().split()))
#
# def branch(target) :
#     branch = 0
#     for i in range(0, n):
#         if tree[i] <= target :
#             continue
#         elif tree[i] > target :
#             branch += (tree[i] - target)
#
#     return branch
#
# target = max(tree)
#
# while 1 :
#     if branch(target) < m :
#         target -= 1
#     elif branch(target) >=m :
#         print(target)
#         break



def bin_search(tree) :
    start = 0
    end = max(tree)
    while start <= end :
        mid = (start + end) // 2

        sum = 0
        for i in range(0, n) :
            if tree[i] > mid :
                sum += tree[i] - mid

        if sum < m :
            end = mid - 1
        else :
            start = mid + 1

    print(end)

bin_search(tree)