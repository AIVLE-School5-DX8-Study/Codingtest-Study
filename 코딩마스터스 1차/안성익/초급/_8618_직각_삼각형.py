import sys
ep = 1e-9
L = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
c = L[0]**2
a_b = L[1]**2 + L[2]**2
if -ep <= (c - a_b) <= ep:
    print('YES')
else:
    print('NO')