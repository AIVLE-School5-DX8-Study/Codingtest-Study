import sys
_, N= sys.stdin.readline().split()
L = sys.stdin.readline().split()
for idx, s in enumerate(L):
    if s == N:
        print(idx+1)
        break