import sys
from itertools import combinations
from collections import deque

def find_jaguar() -> list:
    jaguar = []
    for x in range(N):
        for y in range(M):
            if MAP[x][y]=='2':
                jaguar.append((x, y))

    return jaguar

def update_jaguar_area(visited:list) -> None:
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    queue = deque()
    for x, y in loc_jaguar:
        queue.append((x, y))
        visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if visited[nx][ny]==0:
                if MAP[nx][ny]!='1':
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

def cal_safe_area() -> int:
    visited = [[0] * M for _ in range(N)]
    update_jaguar_area(visited)
    
    ans = 0
    for i in range(N):
        for j in range(M):
            if MAP[i][j]=='0':
                if visited[i][j]==0:
                    ans += 1

    return ans

N, M = map(int, sys.stdin.readline().split())
MAP = [sys.stdin.readline().split() for _ in range(N)]

ans = 0

loc_jaguar = find_jaguar()
empty_area = [(i, j) for i in range(N) for j in range(M) if MAP[i][j]=='0']
comb = combinations(empty_area, 3)

for fences in comb:
    for x, y in fences:
        MAP[x][y] = '1'
    
    ans = max(ans, cal_safe_area())
    
    for x, y in fences:
        MAP[x][y] = '0'

print(ans)