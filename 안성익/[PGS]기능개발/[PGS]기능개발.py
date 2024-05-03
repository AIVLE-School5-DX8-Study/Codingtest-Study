from math import ceil

def solution(progresses, speeds):
    days = [0 for _ in range(len(progresses))]
    for i, p, s in zip(range(len(progresses)), progresses, speeds):
        days[i] = ceil((100-p)/s)
    
    visited = [False] * len(progresses)
    ans = []
    d = 0
    for i, day in enumerate(days):
        if not visited[i]:
            ans.append(count_lower_val(i, visited, days))
    return ans

def count_lower_val(start, visited, days):
    visited[start] = True
    cnt = 0
    for i in range(start, len(visited)):
        if days[i] > days[start]:
            return cnt
        else:
            visited[i] = True
            cnt += 1
    return cnt