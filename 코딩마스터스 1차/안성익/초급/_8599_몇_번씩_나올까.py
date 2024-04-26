import sys
N = int(sys.stdin.readline())
a = '0123456789'
L = [str(i) for i in range(1, N+1)]
d = {i:0 for i in range(10)}
for s in L:
    for i, si in enumerate(a):
        d[i] += s.count(si)

for v in d.values():
    sys.stdout.write(f'{v} ')