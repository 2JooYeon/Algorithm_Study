def LCS (a, b):
  m=len (a)
  n=len (b)
  c=[[0 for i in range (n + 1)] for j in range (m + 1)]
  flag=[[0 for i in range (n + 1)] for j in range (m + 1)]
  for i in range (m):
    for j in range (n):
      if a [i] == b [j]:
        c [i + 1] [j + 1]=c [i] [j] +1
        flag [i + 1] [j + 1]="ok"
      elif c [i + 1] [j]>c [i] [j + 1]:
        c [i + 1] [j + 1]=c [i + 1] [j]
        flag [i + 1] [j + 1]="left"
      else:
        c [i + 1] [j + 1]=c [i] [j + 1]
        flag [i + 1] [j + 1]="up"
  return c, flag

def LCSLength(X, Y):
    m = len(X)
    n = len(Y)
 
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
 
    return T[m][n]

def PrintLCS (flag, a, i, j):
  if i == 0 or j == 0:
    return
  if flag [i] [j] == "ok":
    PrintLCS (flag, a, i-1, j-1)
    print (a [i-1], end="")
  elif flag [i] [j] == "left":
    PrintLCS (flag, a, i, j-1)
  else:
    PrintLCS (flag, a, i-1, j)


X = "ABCBDAB"
Y = "BDCABA"
m = len(X)
n = len(Y)
c, flag = LCS(X, Y)

lcslength = LCSLength(X,Y)
print("LCS-Length : ",lcslength)
print("Print-LCS : ", end=' ')
PrintLCS(flag, X, m, n)

