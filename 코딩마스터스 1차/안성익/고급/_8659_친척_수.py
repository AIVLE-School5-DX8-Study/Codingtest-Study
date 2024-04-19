import sys
N = int(sys.stdin.readline())
L = [int(sys.stdin.readline()) for _ in range(N)]
ans = set()
for i in range(1, 10000):
    r = set()
    for j in L:
        r.add(j % i)
    if len(r) == 1:
        ans.add(i)
print(*ans)