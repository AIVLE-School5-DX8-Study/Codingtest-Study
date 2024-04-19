import sys

N, M = map(int, sys.stdin.readline().split())
g = [[0]*N for _ in range(N)]
e = []
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    e.append((i, j))
for x, y in e:
    g[x-1][y-1], g[y-1][x-1] = 1, 1
for l in g:
    sys.stdout.write(f"{' '.join(map(str, l))}\n")