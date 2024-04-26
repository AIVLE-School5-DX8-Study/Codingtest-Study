import sys
from math import inf
from itertools import combinations, combinations_with_replacement
def divide_N(N:int)->iter:
    l = []
    for i in range(N+1):
        l.append((i, N-i))
    return l
def cnt_W(MAT:iter)->int:
    cnt = 0
    for l in MAT:
        for s in l:
            if s=='W':
                cnt += 1
    return cnt

def reverse_row(MAT:iter, reverseList:iter)->iter:
    M = MAT.copy()
    for i in reverseList:
        for j, m in enumerate(M[i]):
            if m == 'W':
                M[i][j] = 'B'
            else:
                M[i][j] = 'W'
    return M
def reverse_col(MAT:iter, reverseList:iter)->iter:
    M = list(map(list, zip(*MAT)))
    for i in reverseList:
        for j, m in enumerate(M[i]):
            if m == 'W':
                M[i][j] = 'B'
            else:
                M[i][j] = 'W'
    M = list(map(list, zip(*M)))
    return M

N = int(sys.stdin.readline())
MAT = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
ans = inf

for n in range(N+1):
    number_of_reverse = divide_N(n)
    for x, y in number_of_reverse:
        reverse_list_row = list(combinations(range(N), x))
        reverse_list_col = list(combinations(range(N), y))
        max_range = max(len(reverse_list_row), len(reverse_list_col))
        order = combinations_with_replacement(range(max_range), 2)
        for i, j in order:
            if i < len(reverse_list_row) and j < len(reverse_list_col):
                M = MAT.copy()
                M2 = MAT.copy()
                M = reverse_row(M, reverse_list_row[i])
                M = reverse_col(M, reverse_list_col[j])
                M2 = reverse_col(M2, reverse_list_col[j])
                M2 = reverse_row(M2, reverse_list_row[i])
                ans = min(ans, cnt_W(M), cnt_W(M2))
        
sys.stdout.write(f'{ans}')