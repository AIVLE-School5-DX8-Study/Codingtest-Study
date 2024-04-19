import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
capacity = [[0]*N for _ in range(N)]
flow = [[0]*N for _ in range(N)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    capacity[i-1][j-1], capacity[j-1][i-1] = 1, 1

def maxFlow(source:int, sink:int, capacity:list, flow:list) -> int:
    ans = 0
    while True:
        visited = [-1 for _ in range(N)]
        queue = deque([source])
        while queue:
            x = queue.popleft()
            for y in range(N):
                if (capacity[x][y] - flow[x][y] > 0) and visited[y] == -1:
                    queue.append(y)
                    visited[y] = x
                    if y == sink:
                        break
        if visited[sink] == -1:
            break
        
        _flow = float('inf')
        s = sink
        while s != source:
            _flow = min(_flow, capacity[visited[s]][s] - flow[visited[s]][s])
            s = visited[s]
        
        s = sink
        while s != source:
            flow[visited[s]][s] += _flow
            flow[s][visited[s]] -= _flow
            s = visited[s]
        ans += _flow
    return ans

print(maxFlow(0, 1, capacity, flow))