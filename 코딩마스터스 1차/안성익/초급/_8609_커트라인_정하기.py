import sys
def f(arr:iter, arr_len:int, lim:int)->int:
    arr_len -= 1
    ans = min(arr)-1
    scr_lst = [100] + sorted(arr, reverse=True)
    old_cnt = -1
    for scr in scr_lst:
        pass_lst = [False]*(arr_len+1)
        for idx, num in enumerate(arr):
            if num >= scr:
                if idx == 0:
                    pass_lst[0], pass_lst[1]  = [True]*2
                elif idx == arr_len:
                    pass_lst[arr_len-1], pass_lst[arr_len]= [True]*2
                else:
                    pass_lst[idx-1], pass_lst[idx], pass_lst[idx+1] = [True]*3
        cnt = pass_lst.count(True)
        if cnt <= lim:
            if cnt != old_cnt:
                ans = scr
                old_cnt = cnt
    return ans

N, K = map(int, sys.stdin.readline().split())
L = tuple(map(int, sys.stdin.readline().split()))
if N >= 2:
    print(f(L, N, K))
elif N == 1:
    print(L[0])