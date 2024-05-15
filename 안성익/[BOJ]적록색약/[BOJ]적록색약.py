import sys
from collections import deque

def main() -> None:
    N = int(sys.stdin.readline())
    graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    visited_blind = [[False]*N for _ in range(N)]
    area = 0
    area_blind = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                area += bfs(i, j, graph, visited, N, False)
            if not visited_blind[i][j]:
                area_blind += bfs(i, j , graph, visited_blind, N, True)

    print(area, area_blind)

def bfs(x: int, y: int, graph: list, visited: list, limit: int, blind: bool) -> int:
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    queue = deque([(x, y)])
    color = graph[x][y]
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0<=nx<limit) and (0<=ny<limit) and not visited[nx][ny]:
                if not blind:
                    if graph[nx][ny]==color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                else:
                    color = 'R' if color in {'R', 'G'} else 'B'
                    color2 = 'R' if graph[nx][ny] in {'R', 'G'} else 'B'
                    if color2==color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
 
    return 1

if __name__ == '__main__':
    main()