# 입력 받기
n_testcase = int(input())
for _ in range(n_testcase):
    m, n, k = map(int, input().split())
    # field = [[0]*m]*n 으로 초기화하면 특정 셀을 참조할 때 모든 행의 같은 열을 참조하게 되는 오류가 발생. 이유 모름.
    field = []
    for _ in range(n):
        field.append([0]*m)
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            to_visit = []
            if field[i][j] == 1:
                to_visit.append((i, j))
                count += 1
            
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            while len(to_visit) != 0:
                y, x = to_visit.pop()
                if field[y][x] == 1:
                    field[y][x] = 0
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < m and 0 <= ny < n and field[ny][nx] == 1:
                            to_visit.append((ny, nx))

    print(count)
        