import sys
from collections import deque

def dfs(x:int, y:int, graph:list) -> bool:
    if x<0 or x>=10 or y<0 or y>=20:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y, graph)
        dfs(x+1, y, graph)
        dfs(x, y-1, graph)
        dfs(x, y+1, graph)
        return True
    return False

def bfs(x:int, y:int, graph:list) -> int:
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    queue = deque([(x, y)])
    graph[x][y] = 1
    result = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or nx>9 or ny<0 or ny>19:
                    continue
                if graph[nx][ny]==0:
                    graph[nx][ny] = 1
                    queue.append((nx, ny))
                    result += 1
    return 1 if result >= 6 else 0

def count_area_cond1(blueprint:list) -> int:
    graph = [[0]*20 for _ in range(10)]
    for i, line in enumerate(blueprint):
        for j, s in enumerate(line):
            if s != '.':
                graph[i][j] = 1
    result = 0
    
    for i in range(10):
        for j in range(20):
            if dfs(i, j, graph):
                result += 1
    
    if result > 1:
        return 0
    return result

def count_area_cond2(blueprint:list) -> int:
    graph = [[0]*20 for _ in range(10)]
    result = 0
    
    for i, line in enumerate(blueprint):
        for j, s in enumerate(line):
            if s != '#':
                graph[i][j] = 1
    for i in range(10):
        for j in range(20):
            if graph[i][j] == 0:
                temp = bfs(i, j, graph)
                result += temp
    return result

def cond1(blueprint:list) -> int: 
    return 1 if count_area_cond1(blueprint) else 0

def cond2(blueprint:list) -> int:
    return 2 if count_area_cond2(blueprint) >= 2 else 0

N = int(sys.stdin.readline())
blueprints = []

for _ in range(N):
    blueprint = []
    for _ in range(10):
        blueprint.append(sys.stdin.readline().rstrip())
    blueprints.append(blueprint)

for blueprint in blueprints:
    print(cond1(blueprint) + cond2(blueprint))