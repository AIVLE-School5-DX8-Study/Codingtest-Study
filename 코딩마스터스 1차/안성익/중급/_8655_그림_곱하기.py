import sys
from math import gcd
N, M = map(int, sys.stdin.readline().split())
picture = [sys.stdin.readline().rstrip() for _ in range(N)]
z = sorted([i for i in range(1, max(N, M)+1) if (N%i == 0) and (M%i == 0)], reverse=True)

for i in z:
    part = []
    n = N//i
    for k in range(n):
        part.append(picture[k][:M//i] * (i))
    part = part*(N//n)
    if part == picture:
        break
for ii in range(N//i):
    print(picture[ii][:M//i])