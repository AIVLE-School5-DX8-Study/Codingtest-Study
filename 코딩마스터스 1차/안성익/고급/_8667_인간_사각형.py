import sys
input = sys.stdin.readline
N, M = map(int, input().split())
students = [input().split() for _ in range(N)]
ans = 1
for i in range(N):
    for j in range(M):
        for x in range(1, min(N-i, M-j)):
            if students[i][j] == students[i][j+x] == students[i+x][j] == students[i+x][j+x]:
                ans = max(ans, (x+1)*(x+1))
print(ans)