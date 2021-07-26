import sys


def result(a, b) :
    res = 0;

    if (a % 10 == 1) :
        res = 1;
        
    elif (a % 10 == 2) :
        if (b % 4 == 0) : res = 6;
        elif (b % 4 == 1) : res = 2;
        elif (b % 4 == 2) : res = 4;
        else : res = 8;
        
    elif (a % 10 == 3) :
        if (b % 4 == 0) : res = 1;
        elif (b % 4 == 1) : res = 3;
        elif (b % 4 == 2) : res = 9;
        else : res = 7;
        
    elif (a%10 == 4) :
        if (b % 2 == 0) : res = 6;
        else : res = 4;
        
    elif (a % 10 == 5) :
        res = 5;
        
    elif (a % 10 == 6) :
        res = 6;
        
    elif (a % 10 == 7) :
        if (b % 4 == 0) : res = 1;
        elif (b % 4 == 1) : res = 7;
        elif (b % 4 == 2) : res = 9;
        else : res = 3;
        
    elif (a % 10 == 8) :
        if (b % 4 == 0) : res = 6;
        elif (b % 4 == 1) : res = 8;
        elif (b % 4 == 2) : res = 4;
        else : res = 2;
        
    elif (a % 10 == 9) :
        if (b % 2 == 0) : res = 1;
        else : res = 9;
        
    else :
        res = 10;
    
    return res;

data_cnt = int(sys.stdin.readline())
for _ in range(data_cnt):
    a, b = map(int, sys.stdin.readline().split())
    value = result(a, b)
    print(value)


# import sys
# data_cnt = int(sys.stdin.readline())
# for _ in range(data_cnt):
#     a, b = map(int, sys.stdin.readline().split())
#     result = [(a ** i) % 10 for i in range(1,5)][(b % 4) -1]
#     print(result if result != 0 else 10)