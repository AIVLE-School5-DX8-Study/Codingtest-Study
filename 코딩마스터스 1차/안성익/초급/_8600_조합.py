import sys
a, b = map(int, sys.stdin.readline().split())
ans  = 1
for i in range(a, a-b, -1):
    ans *= i
for j in range(2, b+1):
    ans //= j
print(ans)