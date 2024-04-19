import sys
N = int(sys.stdin.readline())
for i in range(1, 7):
    for j in range(1, 7):
        if i+j == N:
            sys.stdout.write(f'{i} {j}\n')