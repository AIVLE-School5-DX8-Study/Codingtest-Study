import sys
from math import floor, ceil
X, Y = map(int, sys.stdin.readline().split())
original_rate = floor(Y/X*100)/100
XX = X
lim = X+1000000000
if floor((Y+1000000000)/(X+1000000000)*100)/100 == original_rate:
    print(-1)
else:
    N = 0
    if 99*X-100*Y > 0: 
        N = ceil((X*X)/(99*X-100*Y))
    if N > 1000000000:
        print(-1)
        exit()
    while X+N <= lim:
        N_old = N
        N -= 1
        if floor((Y+N)/(X+N)*100)/100 != original_rate:
            continue
        else:
            print(N_old)
            break