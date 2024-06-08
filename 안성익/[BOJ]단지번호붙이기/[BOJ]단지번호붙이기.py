import sys
from collections import deque
input = sys.stdin.readline

def main() -> None:
    N = int(input())
    graph = [list(map(int, input().rstrip())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and not visited[i][j]:
                result.append(bfs(graph, visited, i, j, N))
    print(len(result))
    print(*sorted(result), sep='\n')

def bfs(graph: list, visited: list, x: int, y: int, n: int) -> int:
    size = 0
    directions = (
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    )

    queue = deque([(x, y)])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        size += graph[x][y]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    return size

if __name__ == '__main__':
    main()