def solution(n, computers):
    answer = 0
    visited = [[1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                visited[i][j] = 0
    
    def dfs(start, computers, visited):
        visited[start][start] = 1
        for i in range(n):
            if not visited[start][i] and computers[start][i]:
                visited[start][i] = 1
                visited[i][start] = 1
                dfs(i, computers, visited)
    
    for i in range(n):
        if 0 in visited[i]:
            answer+=1
            dfs(i, computers, visited)
            
    return answer
