def solution(arr):
    answer = [arr[0]]
    index = 0
    for n in arr[1:]:
        if answer[index] != n:
            answer.append(n)
            index += 1
    return answer
