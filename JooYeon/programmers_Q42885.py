def solution(people, limit):
    answer = 0
    small = 0
    big = len(people) - 1

    people.sort()

    while small <= big:
        answer += 1
        if people[small] + people[big] <= limit:
            small += 1
        big -= 1

    return answer