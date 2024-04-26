import sys
N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
_sum = sum(L)
_max = max(L)
while _sum > M:
    _max -= 1
    for i, num in enumerate(L):
        if num > _max:
            L[i] = _max
    _sum = sum(L)
sys.stdout.write(f'{_max}')