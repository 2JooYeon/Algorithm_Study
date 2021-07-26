def Q1() :
    n = float(input("n = "))
    k = 0
    num = 2
    while num <= n :
        num = num * 2
        k += 1

    print("Largest Positive Integer k =", k)

###################################################

def Q2() :
    s = input("input word = ")
    result = (s == s[::-1])
    print(result)

###################################################
# Q3 = 5
###################################################

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid - 1
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
    return -1

def Q4() :
    arr = [12, 34, 37, 45, 57, 82, 99, 120, 134]
    print("input arr :",arr)
    binsearch = binary_search(arr, 120)
    print(f"120 is in arr[{binsearch}]")

###################################################

def clockwise_90(arr):
    lennum = len(arr)
    ret = [[0] * lennum for _ in range(lennum)]

    for r in range(lennum):
        for c in range(lennum):
            ret[c][lennum-1-r] = arr[r][c]
    return ret

import random
def Q5() :
    arr = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]
    print("---------------------------------------------")
    print("< Initial 5 * 5 Random Array >")
    for i in range(5) :
        print("  ", arr[i])
    print("---------------------------------------------")
    arr = clockwise_90(arr)
    print("< Rotate the array by 90 degrees clockwise >")
    for i in range(5):
        print("  ", arr[i])
    print("---------------------------------------------")

###################################################

def pairSum(arr, target) :
    lennum = len(arr)

    pair = []
    for i in range(lennum) :
        for j in range(i+1, lennum) :
            if arr[i] + arr[j] == target :
                if arr[j] < 0 :
                    pair.append(str(arr[i]) + str(arr[j]))
                else :
                    pair.append(str(arr[i]) + "+" + str(arr[j]))
    return  pair

def Q6() :
    arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
    print("arr =", arr)
    print("target number =", 7)
    print(">> pairSum =", pairSum(arr, 7))
