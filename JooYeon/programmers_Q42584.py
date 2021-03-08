def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        target = prices[i]
        count = 0
        for j in range(i + 1, len(prices)):
            if target <= prices[j]:
                count += 1
            elif target > prices[j]:
                count += 1
                answer.append(count)
                break
            if j == (len(prices) - 1):
                answer.append(count)
    answer.append(0)
    return answer