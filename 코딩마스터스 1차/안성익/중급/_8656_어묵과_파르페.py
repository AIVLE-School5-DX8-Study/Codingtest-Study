import sys
from collections import deque
def rindex(deq:deque, aim:str)->int:
    for i in range(len(deq)-1, -1, -1):
        if deq[i] == aim:
            return i
    return -1

S = deque(sys.stdin.readline().rstrip())
N = S.count('F')
ans = 0
i = 0
sw = [True]*2

while i < N:
    if sw[0]:
        ld = S.index('F')
        sw[0] = False
    if sw[1]:
        rd = len(S) - rindex(S, 'F') - 1
        sw[1] = False
    if rd <= ld:
        for _ in range(rd):
            ans += 1
            S.pop()
        S.pop()
        i += 1
        sw[1] = True
    else:
        for _ in range(ld):
            ans += 1
            S.popleft()
        S.popleft()
        i += 1
        sw[0] = True
sys.stdout.write(f'{ans}')