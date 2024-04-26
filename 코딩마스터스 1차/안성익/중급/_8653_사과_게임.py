import sys
N, M = list(map(int, sys.stdin.readline().split()))
MAT = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def isTen(arr:list, starindex:tuple, endindex:tuple)->bool:
    result = 0
    for i in range(starindex[0], endindex[0]):
        result += sum(MAT[i][starindex[1]:endindex[1]])
    return True if result == 10 else False

ans = 0
for i in range(N+1):
    for j in range(M+1):
        for ii in range(i+1, N+1):
            for jj in range(j+1, M+1):
                if isTen(MAT, starindex=(i, j), endindex=(ii, jj)):
                    ans += 1
print(ans)