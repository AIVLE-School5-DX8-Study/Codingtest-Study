import sys
from collections import deque

color = {'red':0, 'blue':0}
def count_color_by_bfs(x:int, y:int, color:dict, graph:list, drawing:list) -> None:
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    red, blue = 0, 0
    queue = deque([(x, y)])
    graph[x][y] = 1
    if drawing[x][y] == 'A':
        red += 1
    elif drawing[x][y] == 'B':
        blue += 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
                if drawing[nx][ny] == 'A':
                    red += 1
                elif drawing[nx][ny] == 'B':
                    blue += 1
    if red > blue:
        color['red'] += red
    else:
        color['blue'] += blue
        
    return None

N, M = map(int, sys.stdin.readline().split())
drawing = [sys.stdin.readline().rstrip() for _ in range(N)]
graph = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if drawing[i][j] == 'X':
            graph[i][j] = 1

for x in range(N):
    for y in range(M):
        if graph[x][y] == 0:
            count_color_by_bfs(x, y, color, graph, drawing)

print(*color.values())