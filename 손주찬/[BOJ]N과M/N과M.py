# function
def NM(N, M, result, visited):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, N+1):
        if visited[i]:
            continue
        result.append(i)
        visited[i] = True
        NM(N, M, result, visited)
        result.pop()
        visited[i] = False

# input
N, M = map(int, input().split())

# visited
visited = [False] * (N +1)

# save the result
result = []

# result
NM(N, M, result, visited)