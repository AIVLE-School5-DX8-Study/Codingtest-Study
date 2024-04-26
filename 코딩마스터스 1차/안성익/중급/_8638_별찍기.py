import sys
N = int(sys.stdin.readline())
dic = {1:['*'], 2:[['*', ' ', '*'], [' ', '*', ' '], ['*', ' ', '*']]}
def stars(N:int)->list:
    if N in dic.keys():
        return dic[N]
    else:
        tmp = stars(N-1)
        dic[N] = [[] for _ in range(3**(N-1))]
        row = list(range(3**(N-2)))*3**(N-2)
        col = [0]*3**(N-2) + [1]*3**(N-2) + [0]*3**(N-2)
        for idx, r, c in zip(range(3**(N-1)), row, col):
            if c==0:
                dic[N][idx] += tmp[r] + [' ']*3**(N-2) + tmp[r]
            elif c==1:
                dic[N][idx] += [' ']*3**(N-2) + tmp[r] + [' ']*3**(N-2)
        return dic[N]                
    
ans = stars(N)
for l in ans:
    print(''.join(l))