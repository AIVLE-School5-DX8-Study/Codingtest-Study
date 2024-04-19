import sys
def trans(s:str):
    if s == 'T':
        return 0
    else:
        return 1
MAT = [[1, 0, 1, 0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0, 1, 0, 1]]
M = [list(map(trans, list(sys.stdin.readline()))) for _ in range(8)]
ans = 0
for i in range(8):
    for j in range(8):
        if M[i][j] & MAT[i][j]:
            ans += 1
sys.stdout.write(str(ans))