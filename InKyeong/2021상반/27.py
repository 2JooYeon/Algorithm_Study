def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs(result, idx):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(result + numbers[idx], idx + 1)
            dfs(result - numbers[idx], idx + 1)

    dfs(0, 0)
    return answer