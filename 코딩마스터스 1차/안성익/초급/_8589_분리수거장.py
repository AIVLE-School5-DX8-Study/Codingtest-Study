import sys
from math import inf
def evaluate(d:dict, std:int):
    ans = 0
    for D, peo in d.values():
        ans += abs(std-D)*peo
    return ans
N = int(sys.stdin.readline())
d = {}
for i in range(1, N+1):
    D, peo = map(int, sys.stdin.readline().split())
    d[i] = (D, peo)
_min = inf
min_i = -1
for n, val in d.items():
    ans = evaluate(d, val[0])
    if ans < _min:
        min_i = n
        _min = ans
print(min_i)