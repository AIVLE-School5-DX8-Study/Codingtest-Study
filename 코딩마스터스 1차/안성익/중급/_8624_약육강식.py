import sys

N = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
dp = [0]*(N+1)
for i in range(1, N):
    for j in range(i):
        if s[j] < s[i]:
            dp[i] = max(dp[i], dp[j] + 1)
ans = max(dp)
ans = ans + 1 if ans > 1 else ans
sys.stdout.write(f'{ans}') 