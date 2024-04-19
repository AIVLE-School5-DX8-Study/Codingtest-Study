import sys
d = {2:3}
def tile(N:int)->int:
    if N in d.keys():
        return d[N]
    else:
        ans = tile(N-2)*3+2
        for i in range(N-4, 1, -2):
            ans += tile(i)*2
        d[N] = ans
        return ans

N = int(sys.stdin.readline())
if (N%2):
    sys.stdout.write('0')
    exit()
else:
    sys.stdout.write(f'{tile(N)}')