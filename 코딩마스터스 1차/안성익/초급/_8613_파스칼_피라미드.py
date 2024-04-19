import sys
def ABC(x:int, y:int, z:int):
    ans = 1
    for i in range(2, x+y+z+1):
        ans *= i
    for i in range(2, x+1):
        ans //= i
    for i in range(2, y+1):
        ans //= i
    for i in range(2, z+1):
        ans //= i
    return ans
N = int(sys.stdin.readline())

for i in range(N-1, -1, -1):
    xl  = range(i,-1,-1)
    yl = [N-i-1]*(i+1)
    zl = range(i+1)
    for x,y,z in zip(xl, yl, zl):
        sys.stdout.write(f'{ABC(x,y,z)} ')
    sys.stdout.write('\n')