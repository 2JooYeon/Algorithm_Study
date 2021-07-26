def fibo(n):
	fiboarr = []
	for i in range(0,n):
		if i < 2:
			fiboarr.append(1)
		else:
			fiboarr.append(fiboarr[i-1] + fiboarr[i-2])
	return fiboarr[i]
beta5 = fibo(5)
beta10 = fibo(10)

# print("n = 5 | result =", beta5)
# print("n = 10 | result = ",beta10)

################################################################

# from random import *

# def Corder(p):
#     num = len(p)
#     m = [[0 for x in range(num)] for x in range(num)]
#     s = [[0 for x in range(num)] for x in range(num)]
#     for l in range(2, num):
#         for i in range(1, num - l + 1):
#             j = i + l - 1
#             m[i][j] = float('inf')
#             for k in range(i, j):
#                 q = m[i][k] + m[k + 1][j] + \
#                 	p[i - 1] * p[k] * p[j]
#                 if q < m[i][j]:
#                     m[i][j] = q
#                     s[i][j] = k
#     return (m, s)

# def PrintOrder(s, start, end):
#     if start == end:
#         print('A[{}]'.format(start), end='')
#         return 
#     k = s[start][end]
#     print('( ', end='')
#     PrintOrder(s, start, k)
#     PrintOrder(s, k + 1, end)
#     print(' )', end='')
#     return str

# def Product (A, B, p, q, r):
#     C = [[0]*r for _ in range(p)]
#     for i in range(0, p):
#         for j in range(0, r):
#             for k in range(0, q):
#                 C[i][j] += A[i][k] * B[k][j]
#     return C


# arr = [5,3,7,10]

# a1 = [[0]*3 for _ in range(0, 5)]
# a2 = [[0]*7 for _ in range(0, 3)]
# a3 = [[0]*10 for _ in range(0, 7)]

# print('[ A[1] : 5 X 3 Matrix ]')
# for i in range(0, 5):
#     for j in range(0, 3):
#         a1[i][j]= randint(1,99)
#         print(a1[i][j]," ", end='')
#     print("\n")
# print("\n")
# print('[ A[2] : 3 X 7 Matrix ]')
# for i in range(0, 3):
#     for j in range(0, 7):
#         a2[i][j]= randint(1,99)
#         print(a2[i][j]," ", end='')
#     print("\n")
# print("\n")
# print('[ A[3] : 7 X 10 Matrix ]')
# for i in range(0, 7):
#     for j in range(0, 10):
#         a3[i][j]= randint(1,99)
#         print(a3[i][j]," ", end='')
#     print("\n")
# print("\n")

# (m,s) = Corder(arr)

# print('[ Output matrix ]')
# beforeOuput = Product(a2,a3,3,7,10)
# output = Product(a1,beforeOuput,5,3,10)
# for i in range(0, 5):
#     for j in range(0, 10):
#         print(output[i][j]," ", end='')
#     print("\n")
# print('[ Optimal chain order ]')
# chainOrder = PrintOrder(s, 1, 3)
# print("\n")
# print('[ Minimum number of computation ]')
# print(m[1][3])

##########################################################

def Backpack(limit, data_list):
    data_list = sorted(data_list, key = lambda x:x[1] / x[0], reverse=True)
    totalNum = 0
    details = list() 
    print('>> Sort decreasing order : ', data_list)

    for data in data_list:
        if limit - data[0] >= 0:
            limit -= data[0]
            totalNum += data[1]
            details.append([data[0], data[1], 1])
        else:
            fraction = limit / data[0]
            limit -= fraction * data[0]
            totalNum += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break
    return totalNum, details

total, details = Backpack(16, [(6,60), (10,20), (3,12), (5,80), (1,30), (3,60)])
print('>> Maximum value : ', total)
print('>> Items with their fraction numbers : ', details)
