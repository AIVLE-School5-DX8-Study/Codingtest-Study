import sys
from collections import deque
from math import inf

N = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[inf]*N for _ in range(N)]
dp[0][0] = MAP[0][0]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

deq = deque([(0, 0)])
while deq:
    x, y = deq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if dp[nx][ny] > dp[x][y] + MAP[nx][ny]:
            dp[nx][ny] = dp[x][y] + MAP[nx][ny]
            deq.append((nx, ny))

print(dp[N-1][N-1])