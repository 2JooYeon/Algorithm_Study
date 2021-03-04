def solution(clothes):
    answer = 1

    item_count = {}

    for item in clothes:
        if (item[1] not in item_count):
            item_count[item[1]] = 1
        else:
            item_count[item[1]] += 1

    count_list = item_count.values()

    for num in count_list:
        # num+1에서 +1은 아예 선택 안할 수도 있는 경우의 수 고려
        answer *= (num + 1)

    # -1 하는 이유는 의상을 하나도 안입는 경우를 제외하기 위해서
    return answer - 1
