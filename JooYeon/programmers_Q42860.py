def solution(name):
    answer = 0
    index = 0

    name = list(name)

    while 1:
        term = ord(name[index]) - 65

        if 0 < term <= 12:
            answer += term
            name[index] = 'A'
        elif term > 12:
            answer += 25 - term + 1
            name[index] = 'A'

        if not len(list(filter(lambda x: not x == 'A', name))): return answer

        left, right = 0, 0
        for l in range(1, len(name)):
            if name[index-l] == 'A':
                left += 1
            else:
                left += 1
                break
        for r in range(1, len(name)):
            if name[index+r] == 'A':
                right += 1
            else:
                right += 1
                break

        # 왼쪽으로 가야지
        if left < right:
            answer += left
            index -= left
        # 오른쪽으로 가야지
        else:
            answer += right
            index += right

    return answer