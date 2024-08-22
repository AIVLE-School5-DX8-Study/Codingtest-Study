def solution(n, computers):
    def dfs(i):
        visited[i] = 1
        for j in range(n):
            if computers[i][j] and not visited[j]: # unvisited + 인접할 때
                dfs(j)
                
    answer = 0
    visited = [False] * (n)
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            
    return answer

