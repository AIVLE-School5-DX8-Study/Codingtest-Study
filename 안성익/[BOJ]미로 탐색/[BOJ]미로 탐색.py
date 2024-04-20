import sys
from collections import deque

def main():
    N, M = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
    print(bfs(0, 0, (N, M), graph))

def bfs(x: int, y: int, size: tuple, graph: list) -> bool:
    N, M = size[0], size[1]
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0<=nx<M) and (0<=ny<N) and graph[ny][nx]==1:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1]

if __name__ == '__main__':
    main()