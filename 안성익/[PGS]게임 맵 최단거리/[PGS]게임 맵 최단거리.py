from collections import deque

def solution(maps):
    directions = (
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    )
    n = len(maps)
    m = len(maps[0])

    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    return maps[-1][-1] if maps[-1][-1] > 1 else -1