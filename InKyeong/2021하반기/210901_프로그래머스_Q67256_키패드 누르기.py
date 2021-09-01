def solution(numbers, hand):
    answer = ''
    left = [3, 0]
    right = [3, 2]
    for current in numbers:
        print(left, right, current)
        if current == 1 or current == 4 or current == 7:
            answer += "L"
            if current == 1:
                left = [0, 0]
            elif current == 4:
                left = [1, 0]
            elif current == 7:
                left = [2, 0]
        elif current == 3 or current == 6 or current == 9:
            answer += "R"
            if current == 3:
                right = [0, 2]
            elif current == 6:
                right = [1, 2]
            elif current == 9:
                right = [2, 2]
        else:
            leftmove, rightmove = 0, 0

            if left[1] == 0:
                leftmove += 1
            if right[1] == 2:
                rightmove += 1

            if current == 2:
                target = 0
            elif current == 5:
                target = 1
            elif current == 8:
                target = 2
            elif current == 0:
                target = 3

            leftmove += abs(target - left[0])
            rightmove += abs(target - right[0])

            if leftmove > rightmove or (leftmove == rightmove and hand == "right"):
                answer += "R"
                right = [target, 1]
            elif leftmove < rightmove or (leftmove == rightmove and hand == "left"):
                answer += "L"
                left = [target, 1]

    return answer