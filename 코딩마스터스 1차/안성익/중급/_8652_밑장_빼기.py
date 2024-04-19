import sys
from collections import deque
N = int(sys.stdin.readline())
deck = deque(map(int, sys.stdin.readline().split()))
for i in range(1, N+1):
    if i == deck[-1]:
        deck.pop()
    elif i == deck[0]:
        deck.popleft()
    else:
        sys.stdout.write('NO')
        exit()

sys.stdout.write('YES')