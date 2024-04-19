import sys
N = int(sys.stdin.readline())
dp = [[0]*N for _ in range(N)]
M = [list(map(int, sys.stdin.readline().split()))]
dp[0][0] = M[0][0]
for i in range(1, N):
    l = list(map(int, sys.stdin.readline().split()))
    dp[i][0] = dp[i-1][0] + l[0]
    M.append(l)

for i in range(1, N):
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + M[i][j]

print(max(dp[N-1]))