#현대Softeer 사전테스트
# import sys

K,P,N  = input().split()
K = int(K)
P = int(P)
N = int(N)
answer = K
for i in range(1,N+1) :
    answer *= P


print(answer%1000000007)