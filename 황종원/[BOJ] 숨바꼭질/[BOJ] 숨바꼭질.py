from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visit[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not visit[nx]:
                visit[nx] = visit[x] + 1
                q.append(nx)

MAX = 10 ** 5
visit = [0] * (MAX + 1)
n, k = map(int, input().split())

bfs()

