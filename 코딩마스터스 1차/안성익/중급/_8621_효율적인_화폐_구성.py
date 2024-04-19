import sys
N, M = map(int, sys.stdin.readline().split())
L = set([int(sys.stdin.readline()) for _ in range(N)])
dp = [10001] * (M + 1)
dp[0] = 0
for i in L:
    for j in range(i, M + 1):
        if dp[j - i] != 10001:
            dp[j] = min(dp[j], dp[j - i] + 1)
            
if dp[M] == 10001:
    print("-1")
else:
    print(dp[M])