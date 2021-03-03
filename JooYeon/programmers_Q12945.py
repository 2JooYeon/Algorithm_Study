def solution(n):
    result = 0;

    first = 0;
    second = 1;

    for num in range(2, n + 1):
        result = first + second
        first = second
        second = result

    return result % 1234567