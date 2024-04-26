import sys
from collections import deque
N = int(sys.stdin.readline())
n = 1
k = 0
while 1:
    if n > N:
        break
    k += 1
    n *= 2
if k == 1:
    print(N)
    exit()
l = list(map(int, sys.stdin.readline().split()))+[0]*(n-N)
L = deque()
L.append(l)
for _ in range(k):
    ll = []
    for i in range(0, len(l)-1, 2):
        ll.append(l[i]+l[i+1])
    
    l = ll
    L.appendleft(l)
for s in L:
    s = ' '.join(map(str, s))
    print(s)