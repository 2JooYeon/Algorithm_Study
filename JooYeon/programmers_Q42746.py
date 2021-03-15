def solution(numbers):
    answer = ''
    str_numbers = list(map(lambda x: str(x), numbers))
    str_numbers.sort(reverse=True, key=lambda x: x * 3)
    for num in str_numbers:
        answer += num

    if not int(answer):
        return '0'
    else:
        return answer
