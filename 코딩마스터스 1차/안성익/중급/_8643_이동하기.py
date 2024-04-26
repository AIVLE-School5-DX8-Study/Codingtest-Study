def dfs(xi:int, yi:int, xl:int, yl:int, enable_move:int, visited:set) -> int:
    path = 0
    visited.add((xi, yi))
    if enable_move == 0:
        if xi == xl and yi == yl:
            return 1
        else:
            return 0
    for i in range(4):
        visited_copy = visited.copy()
        nx = xi + dx[i]
        ny = yi + dy[i]
        if (nx, ny) not in visited:
            path += dfs(nx, ny, xl, yl, enable_move - 1, visited_copy)
    return path

N = int(input())
xi, yi = map(int, input().split())
xl, yl = map(int, input().split())
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

print(dfs(xi, yi, xl, yl, N, set()))