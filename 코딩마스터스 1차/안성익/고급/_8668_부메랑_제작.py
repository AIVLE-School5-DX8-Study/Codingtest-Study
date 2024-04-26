N, M = map(int, input().split())
material = [list(map(int, input().split())) for _ in range(N)]
positions = (((0, -1, 1), (0, 0, 2), (1, 0, 1)), # ┌
            ((-1, 0, 1), (0, 0, 2), (0, -1, 1)), # ㄱ
            ((0, 1, 1), (0, 0, 2), (0, -1, 1)), # ㄴ
            ((-1, 0, 1), (0, 0, 2), (0, 1, 1)), # ┘
            )

ans = 0

for x in range(N):
    for y in range(M):
        for position in positions:
            strength = 0
            visited = [[0]*N for _ in range(N)]
            for dx, dy, n in position:
                nx, ny = x+dx, y+dy
                if nx<0 or nx>=N or ny<0 or ny>=M:
                    strength = -1
                    break
                visited[nx][ny] = 1
                strength += material[dx][dy] * n
            
            ans = max(ans, strength)

print(ans)