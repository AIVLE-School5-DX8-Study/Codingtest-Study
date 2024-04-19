import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

def is_survived(graph:list, start:int, goal:int, time_limit:int) -> bool:
    visited = set()
    queue = deque([start])
    
    while queue:
        v = queue.popleft()
        if v == goal:
            return True
        for i, limit in graph[v]:
            if i not in visited:
                if limit >= time_limit:
                    visited.add(i)
                    queue.append(i)
    return False

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

start, goal = map(int, sys.stdin.readline().split())
for i in range(1, 101):
    if is_survived(graph, start, goal, i):
        ans = i
    else:
        break
print(ans)