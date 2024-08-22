T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = [(x, y)]
    mtrx[x][y] = 0   # 방문처리
    
    while queue:
        x, y = queue.pop(0)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
                
            if mtrx[nx][ny] == 1:
                queue.append((nx, ny))
                mtrx[nx][ny] = 0

# 행렬 생성           
for i in range(T):
    M, N ,K = map(int, input().split())
    mtrx = [[0]*(N) for _ in range(M)]
    count = 0

    for j in range(K):
        x, y = map(int, input().split())
        mtrx[x][y] = 1
        
    for a in range(M):
        for b in range(N):
            if mtrx[a][b] == 1:
                bfs(a, b)
                count += 1
    
    print(count)
