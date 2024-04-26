import sys

N1, M1 = map(int, sys.stdin.readline().split())
graph1 = [[0]*N1 for _ in range(N1)]
for _ in range(M1):
    u, v = map(int, sys.stdin.readline().split())
    graph1[u-1][v-1], graph1[v-1][u-1] = 1, 1

N2, M2 = map(int, sys.stdin.readline().split())
graph2 = [[0]*(N2) for _ in range(N2)]
for _ in range(M2):
    u, v = map(int, sys.stdin.readline().split())
    graph2[u-1][v-1], graph2[v-1][u-1] = 1, 1

l1 = []
for line in graph1:
    l1.append(line.count(1))
l2 = []

for line in graph2:
    l2.append(line.count(1))

if sorted(l1) == sorted(l2):
    print('YES')
else:
    print('NO')