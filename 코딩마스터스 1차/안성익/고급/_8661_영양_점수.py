import sys
from math import inf
from itertools import combinations
N = int(sys.stdin.readline())
MAT = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

_min = inf
st = set(range(N))
comb = combinations(st, N//2)
for x in comb:
    num1 = num2 = 0
    comb2 = combinations(x, 2)
    comb3 = combinations(st-set(x), 2)
    for (i, j), (x, y) in zip(comb2, comb3):
        num1 += MAT[i][j] + MAT[j][i]
        num2 += MAT[x][y] + MAT[y][x]
    _min = min(_min, abs(num1-num2))
sys.stdout.write(f'{_min}')