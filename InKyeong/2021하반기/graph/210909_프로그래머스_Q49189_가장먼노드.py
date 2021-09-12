def solution(n, vertex):

    checklist = [[] for _ in range(0, n)]
    visited = [False for _ in range(0, n)]
    visited[0] = True
    steplist = [0 for _ in range(0, n)]
    nowlist = [0]

    for a, b in vertex:
        checklist[a - 1].append(b - 1)
        checklist[b - 1].append(a - 1)

    print(checklist)

    while nowlist:
        i = nowlist.pop(0)

        for j in checklist[i]:
            if visited[j] == False:
                visited[j] = True
                nowlist.append(j)
                print(i, j, nowlist)
                steplist[j] = steplist[i] + 1
                print(steplist)

    steplist.sort(reverse=True)
    answer = steplist.count(steplist[0])

    return answer