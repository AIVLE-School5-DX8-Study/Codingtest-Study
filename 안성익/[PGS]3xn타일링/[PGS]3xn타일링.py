import sys
from functools import lru_cache
sys.setrecursionlimit(100_000)
MOD = 1_000_000_007

@lru_cache(None)
def solution(n):
    if n == 0:
        return 0
    elif n == 2:
        return 3
    result = (3*solution(n-2)) % MOD
    for i in range(n-4, 1, -2):
        result += 2*solution(i) % MOD
    return (result + 2) % MOD