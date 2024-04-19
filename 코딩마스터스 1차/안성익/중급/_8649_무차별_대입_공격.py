import sys
from itertools import product
_, M = map(int, sys.stdin.readline().split())
S = sorted(sys.stdin.readline().rstrip())
comb = product(S, repeat=M)
for s in comb:
    sys.stdout.write(''.join(s))
    sys.stdout.write('\n')