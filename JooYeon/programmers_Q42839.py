from itertools import permutations
import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    temp = set()

    num_list = list(numbers)

    for size in range(1, len(num_list) + 1):
        num_result = list(permutations(num_list, size))
        num = list(map(lambda x : int("".join(x)), num_result))
        for value in num:
            if not value == 1 and not value == 0:
                if is_prime(value):
                    temp.add(value)

    return len(temp)
