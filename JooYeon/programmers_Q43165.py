answer = 0

def dfs(numbers, target, index):
    if index <= len(numbers) - 1:
        dfs(numbers, target, index + 1)

        numbers[index] *= -1
        dfs(numbers, target, index + 1)
    else:
        if sum(numbers) == target:
            global answer
            answer += 1
    return answer

def solution(numbers, target):

    return dfs(numbers, target, 0)