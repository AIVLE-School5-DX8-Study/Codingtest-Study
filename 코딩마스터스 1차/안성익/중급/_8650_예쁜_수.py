import sys
number = sys.stdin.readline().rstrip()
N = len(number)
l = set()
for i in range(1, N):
    for j in range(N-i+1):
        l.add(int(number[j:j+i]))

number = int(number)
for d in l:
    if (d != 0) and (not (number % d)):
        sys.stdout.write('YES')
        exit()
sys.stdout.write('NO')