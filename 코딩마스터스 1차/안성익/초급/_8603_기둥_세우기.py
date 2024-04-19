import sys
N, M = map(int, sys.stdin.readline().split())
MAT = [sys.stdin.readline().split() for _ in range(N)]
ans = 0 
for s in MAT:
    if '0' not in s:
        ans += 1
sys.stdout.write(str(ans))