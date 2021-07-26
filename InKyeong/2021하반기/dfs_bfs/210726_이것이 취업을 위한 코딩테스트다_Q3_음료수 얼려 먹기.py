n, m = map(int, input().split())
print(n, m)

graph = [[] for i in range(n)]

for i in range(0, n) :
    s = input()
    for j in range(0, m) :
        graph[i].append(int(s[j]))

def dfs(x, y) :
    if x<0 or x>=n or y<0 or y>=m :
        return False
    if graph[x][y] == 0 :
        graph[x][y] = 1
        print(dfs(x-1, y))
        print(graph)
        print(dfs(x, y-1))
        print(graph)
        print(dfs(x+1, y))
        print(graph)
        print(dfs(x, y+1))
        print(graph)
        return True
    else :
        return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True :
            result += 1

print("result :", result)




