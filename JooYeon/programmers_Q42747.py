def solution(citations):
    answer = 0

    while True:
        answer += 1
        count = 0
        for citation in citations:
            if (citation >= answer):
                count += 1
            if (answer == count):
                break
        if (answer != count):
            return answer - 1;

    return answer