def solution(nums):
    get = len(nums)//2
    if len(set(nums)) >= get:
        return get
    else:
        return len(set(nums))
