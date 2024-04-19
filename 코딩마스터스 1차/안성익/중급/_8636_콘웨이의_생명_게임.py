from copy import deepcopy

def count_around(x:int, y:int)->None:
    cnt = 0
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or ny < 0 or nx > 4 or ny > 4:
            continue
        if life[nx][ny] == '1':
            cnt += 1
    if life[x][y] == '1':
        if cnt not in (2, 3):
            life_copy[x][y] = '0'
    else:
        if cnt == 3:
            life_copy[x][y] = '1'
    return None
            
dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (-1, 0, 1, -1, 1, -1, 0, 1)

N = int(input())
life = [list(input()) for _ in range(5)]

for _ in range(N):
    life_copy = deepcopy(life)
    for i in range(5):
        for j in range(5):
            count_around(i, j)
    life = deepcopy(life_copy)

for l in life:
    print(''.join(l))