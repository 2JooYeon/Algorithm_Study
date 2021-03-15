def solution(brown, yellow):
    answer = []
    brown -= 4
    brown //= 2
    x = y = 0
    for x in range(1, brown):
        for y in range(1, brown):
            if x + y == brown:
                if x * y == yellow:
                    x,y = max([x, y]), min([x,y])
                    answer.append(x + 2)
                    answer.append(y + 2)
                    return answer

