def solution(n, times):
    xi = 0
    xl = n * max(times)
    while xi <= xl:
        xm = (xi+xl)//2
        enable = 0
        for time in times:
            enable += xm//time
            
            if enable >= n:
                break
        if enable >= n:
            answer = xm
            xl = xm - 1
        else:
            xi = xm + 1
    return answer