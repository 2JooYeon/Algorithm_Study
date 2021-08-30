def solution(n, costs):
    sortlist = sorted(costs, key=lambda x: (x[2], x[0]))

    select = set()
    select.add(sortlist[0][0])
    answer = 0

    while len(select) != n:
        for i in sortlist:
            if i[0] in select and i[1] in select:
                continue
            if i[0] in select or i[1] in select:
                select.update([i[0], i[1]])
                answer += i[2]
                break
            else:
                print(i)

    return answer
