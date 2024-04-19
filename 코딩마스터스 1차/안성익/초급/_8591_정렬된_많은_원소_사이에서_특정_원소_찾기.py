import sys

_, A = sys.stdin.readline().split()
L = sys.stdin.readline().split()

for idx, num in enumerate(L):
    if num == A:
        print(idx+1)
        exit()
print(-1)