import sys
d = int(sys.stdin.readline())
N = int(sys.stdin.readline())
D = {str('{:04}'.format(i)):0 for i in range(10000)}
T = (1, 60, 3600)
for _ in range(N):
    num, time = sys.stdin.readline().split()
    D[num] = time
for _ in range(N):
    num, time = sys.stdin.readline().split()
    pre_time = map(int, D[num].split(':'))
    cur_time = map(int, time.split(':'))
    h = 0
    for i, j, k in zip(cur_time, pre_time, T):
        h += (i-j)/k
    D[num] = int(d/h)
for num, time in D.items():
    if time:
        sys.stdout.write(f'{num} {time}\n')