import time

###################################################################

def bubble_sort(arr):

    for i in range(len(arr)):
        flag = True

        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            break

    return arr

###################################################################

def insertion_sort(arr):

    for i in range(1, len(arr)):

        comp = arr[i]
        j = i - 1

        while ( j >= 0 and arr[j] > comp ):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = comp
    answer = arr
    return answer

###################################################################

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    merge_arr = []
    l = h = 0
    while l < len(left_arr) and h < len(right_arr):
        if left_arr[l] < right_arr[h]:
            merge_arr.append(left_arr[l])
            l += 1
        else:
            merge_arr.append(right_arr[h])
            h += 1
    merge_arr += left_arr[l:]
    merge_arr += right_arr[h:]
    return merge_arr

###################################################################

from random import randint

def quick_sort(arr):

    if len(arr) < 2:
        return arr

    low, same, high = [], [], []
    pivot = arr[randint(0, len(arr) - 1)]

    for item in arr:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)


    return quick_sort(low) + same + quick_sort(high)    

###################################################################

def counting_sort(arr, digit):
    n = len(arr)

    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = int(arr[i]/digit) 
        count[ (index)%10 ] += 1

    for i in range(1,10):
        count[i] += count[i-1]  

    i = n - 1
    while i >= 0:
        index = int(arr[i]/digit)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1


    for i in range(0,len(arr)): 
        arr[i] = output[i]
 
def radix_sort(arr):
    maxValue = max(arr)  
    digit = 1
    while int(maxValue/digit) > 0: 
        counting_sort(arr,digit)
        digit *= 10
    return arr

###################################################################

def insertion(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up    
    return b    
             
def bucket_sort(x):
    arr = []
    if len(x) == 100 :
        slot_num = 10
    elif len(x) == 1000 :
        slot_num = 20
    elif len(x) == 10000 :
        slot_num = 50

    for i in range(slot_num):
        arr.append([])
         
    for j in x:
        if len(x) == 100 :
            index_b = int((j-1)/10)
        elif len(x) == 1000 :
            index_b = int((j-1)/50)
        elif len(x) == 10000 :
            index_b = int((j-1)/200)
        arr[index_b].append(j)

    for i in range(slot_num):
        arr[i] = insertion(arr[i])
         
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x

###################################################################

def checkTime(arr1, arr2, arr3, func) :
    print("[ ",str(func)," ]")
    print(">> 1-1) initial input array")
    print(arr1)
    startTime1 = time.time()
    ans1 = func(arr1)
    endTime1 = time.time()
    elapsedTime1 = (endTime1 - startTime1) * 1000000
    print(">> 1-2) After sorting array")
    print(ans1)
    print(">> Time : ", elapsedTime1)
    time.sleep(1)
    print(">> 2-1) initial input array")
    print(arr2)
    startTime2 = time.time()
    ans2 = func(arr2)
    endTime2 = time.time()
    elapsedTime2 = (endTime2 - startTime2) * 1000000
    print(">> 2-2) After sorting array")
    print(ans2)
    print(">> Time : ", elapsedTime2)
    time.sleep(1)
    print(">> 3-1) initial input array")
    print(arr3)
    startTime3 = time.time()
    ans3 = func(arr3)
    endTime3 = time.time()
    elapsedTime3 = (endTime3 - startTime3) * 1000000
    print(">> 3-2) After sorting array")
    print(ans3)
    print(">> Time : ", elapsedTime3)
    return elapsedTime1, elapsedTime2, elapsedTime3, ans1, ans2, ans3

def makeArr(num, arr) :
    for i in range(0, num) :
        arr.append(num - i)
    return(arr)

a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3, f1, f2, f3 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

a1 = makeArr(100, a1)
a2 = makeArr(1000, a2)
a3 = makeArr(10000, a3)
at1, at2, at3, ra1, ra2, ra3 = checkTime(a1, a2, a3, bubble_sort)
time.sleep(1) 
b1 = makeArr(100, b1)
b2 = makeArr(1000, b2)
b3 = makeArr(10000, b3)
bt1, bt2, bt3, rb1, rb2, rb3 = checkTime(b1, b2, b3, insertion_sort)
time.sleep(1) 
c1 = makeArr(100, c1)
c2 = makeArr(1000, c2)
c3 = makeArr(10000, c3)
ct1, ct2, ct3, rc1, rc2, rc3 = checkTime(c1, c2, c3, merge_sort)
time.sleep(1) 
d1 = makeArr(100, d1)
d2 = makeArr(1000, d2)
d3 = makeArr(10000, d3)
dt1, dt2, dt3, rd1, rd2, rd3 = checkTime(d1, d2, d3, radix_sort)
time.sleep(1) 
e1 = makeArr(100, e1)
e2 = makeArr(1000, e2)
e3 = makeArr(10000, e3)
et1, et2, et3, re1, re2, re3 = checkTime(e1, e2, e3, quick_sort)
time.sleep(1) 
f1 = makeArr(100, f1)
f2 = makeArr(1000, f2)
f3 = makeArr(10000, f3)
ft1, ft2, ft3, rf1, rf2, rf3 = checkTime(f1, f2, f3, bucket_sort)

print("        |       Bubble       |     Insertion     |       Merge       |        Radix       |        Quick       |       Bucket       |")
print("-------------------------------------------------------------------------------------------------------------------------------------")
print("  100   |", at1,"|", bt1,"|", ct1,"|", dt1,"|", et1,"|", ft1,"|")
print("  1000  |", at2,"|", bt2,"|", ct2,"|", dt2,"|", et2,"|", ft2,"|")
print("  10000 |", at3,"|", bt3,"|", ct3,"|", dt3,"|", et3,"|", ft3,"|")

