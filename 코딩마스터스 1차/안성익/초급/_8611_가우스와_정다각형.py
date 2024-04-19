import sys
K = int(sys.stdin.readline())
while 1:
    if not K%2:
        K //= 2
    else:
        break

if not K%3:
    K //= 3
if not K%5:
    K //= 5
if not K%17:
    K //= 17
if not K%257:
    K //= 257
if not K%65537:
    K //= 65537
if K == 1:
    sys.stdout.write('YES')
else:
    sys.stdout.write('NO')