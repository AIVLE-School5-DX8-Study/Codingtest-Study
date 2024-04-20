m, n = map(int, input().split())
board = list()
for i in range(m):
    board.append(input())

best = 64
for i in range(m-7):
    for j in range(n-7):
        tmp = 0
        for r in range(8):
            for c in range(8):
                if (8*r+c)%2 == 0:
                    if board[i+r][j+c] == 'B':
                        tmp += 1
                else:
                    if board[i+r][j+c] == 'W':
                        tmp += 1
        tmp = min(tmp, 64-tmp)
        best = min(best, tmp)

print(best)