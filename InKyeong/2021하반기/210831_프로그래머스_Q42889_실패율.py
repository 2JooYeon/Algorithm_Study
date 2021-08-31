def solution(N, stages):
    usernum = []
    total = len(stages)

    for i in range(1, N + 1):
        challenger = stages.count(i)
        if total == 0:
            fail = 0
        else:
            fail = challenger / total
        countset = [i, challenger, fail]
        usernum.append(countset)
        total -= challenger

    sortlist = sorted(usernum, key=lambda x: (-x[2], x[0]))
    # print(sortlist)
    answer = list(map(lambda x: x[0], sortlist))

    return answer