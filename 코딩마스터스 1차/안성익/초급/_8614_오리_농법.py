import sys
N = int(sys.stdin.readline())
MAT = [sys.stdin.readline().split() for _ in range(N)]
MAT2 = [l for l in zip(*MAT)]
for l in MAT:
    if '1' not in l:
        for i in range(N):
            l[i] = '0'
for idx, l in enumerate(MAT2):
    if '1' not in l:
        for i in range(N):
            MAT[i][idx] = '0'

ans = 0
for l in MAT:
    ans += l.count('2')
print(ans)