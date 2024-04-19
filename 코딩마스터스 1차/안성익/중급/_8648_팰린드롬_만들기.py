import sys
from itertools import permutations
N = int(sys.stdin.readline())
S = [sys.stdin.readline().rstrip() for _ in range(N)]
order_l = permutations(range(N), N)

for order in order_l:
    s = ''
    for i in order:
        s += S[i]
    if s == s[::-1]:
        sys.stdout.write('YES')
        exit()

sys.stdout.write('NO')