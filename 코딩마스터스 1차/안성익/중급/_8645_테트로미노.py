import sys
TET = [sys.stdin.readline().rstrip() for _ in range(5)]
N = 5
sharp_cnt = 0
for l in TET:
    for s in l:
        if s == '#':
            sharp_cnt += 1
if sharp_cnt != 4:
    print('NO')
    exit()
for s in TET[::-1]:
    if s == '.....':
        TET.pop()
        N -= 1
    else:
        break

for i in range(1, N):
    old_l = TET[i-1]
    sharp_lst = []
    cnt = 0
    for j in range(5):
        if old_l[j] == '#':
            sharp_lst.append(j)
    
    for k in sharp_lst:
        if TET[i][k] == '#':
            cnt += 1
    if (sharp_lst and (not cnt)):
        print('NO')
        exit()
print('YES')