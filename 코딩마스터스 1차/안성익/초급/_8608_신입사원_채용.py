import sys
input = sys.stdin.readline
N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
ans = [1] * N
can_evaluate = []

for i, (x, y) in enumerate(A):
    r = 1
    can_evaluate.append([True]*N)
    for j, (xx, yy) in enumerate(A):
        if i == j:
            continue
        if ((x <= xx) and (y < yy)) or ((x < xx) and (y <= yy)):
            r += 1
        elif ((x >= xx) and (y > yy)) or ((x > xx) and (y >= yy)) :
            continue
        else:
            can_evaluate[i][j] = False
    ans[i] = r

for _ in range(N):
    for i, r in enumerate(ans):
        for j in range(N):
            if can_evaluate[i][j]:
                continue
            r = min(r, ans[j])
            ans[j] = min(ans[j], r)

print(*ans)