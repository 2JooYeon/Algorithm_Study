def solution(participant, completion):
    # 정확성 테스트는 통과하고 효율성 테스트는 실패한 코드
    # for person in participant:
    #     if (person in completion) and (participant.count(person) == completion.count(person)):
    #         continue;
    #     else:
    #         return person

    participant.sort()
    completion.sort()

    check_list = dict(zip(participant, completion))

    for person in participant[0:len(participant) - 1]:
        if check_list[person] != person:
            return person

    return participant[len(participant) - 1]