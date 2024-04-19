def is_win(board):
    directions = ((1, 0), (0, 1), (1, 1), (-1, 1))
    for x in range(10):
        for y in range(10):
            if board[x][y] == 'W':
                for dx, dy in directions:
                    count = 1
                    for i in range(1, 5):
                        nx, ny = x + dx*i, y + dy*i
                        if 0 <= nx < 10 and 0 <= ny < 10 and board[nx][ny] == 'W':
                            count += 1
                        else:
                            break
                    if count == 5:
                        return 1
    return 0

def remove_line(board:list, idx:int, axis:int) -> list:
    if axis == 0:
        temp = board[idx]
        board[idx] = ['.']*10
        return temp
    else:
        temp = []
        for i in range(10):
            temp.append(board[i][idx])
            board[i][idx] = '.'
        return temp

board = [list(input()) for _ in range(10)]
ans = 0

for i in range(10):
    temp = remove_line(board, i, 0)
    for j in range(10):
        for k in range(10):
            if board[j][k] == '.':
                board[j][k] = 'W'
                ans += is_win(board)
                board[j][k] = '.'
    board[i] = temp

for i in range(10):
    temp = remove_line(board, i, 1)
    for j in range(10):
        for k in range(10):
            if board[j][k] == '.':
                board[j][k] = 'W'
                ans += is_win(board)
                board[j][k] = '.'
    for idx, s in enumerate(temp):
        board[idx][i] = s

print(ans)