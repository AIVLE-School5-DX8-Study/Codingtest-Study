import sys
from itertools import combinations

def score(student1:int, student2:int, graph:list) -> int:
    if graph[student1][student2] == 1:
        return 1
    elif graph[student1][student2] == 2:
        return -1
    else:
        return 0

input = sys.stdin.readline
N = int(input())
K = int(input())
graph = [[0]*(2*N) for _ in range(2*N)]
for _ in range(K):
    a, b, c = map(int, input().split())
    graph[b-1][c-1], graph[c-1][b-1] = a, a

ans = float('-inf')
student = set(range(2*N))

if N == 1:
    print(score(0, 1, graph))
elif N == 2:
    comb = combinations(student, 2)
    for a, b in comb:
        c, d = student - set((a, b))
        temp = score(a, b, graph) + score(c, d, graph)
        ans = max(ans, temp)
    print(ans)
elif N == 3:
    comb = combinations(student, 2)
    for a, b in comb:
        comb2 = combinations(student-set((a, b)), 2)
        for c, d in comb2:
            e, f = student - set((a, b, c, d))
            temp = score(a, b, graph) + score(c, d, graph) + score(e, f, graph)
            ans = max(ans, temp)
    print(ans)
else:
    comb = combinations(student, 2)
    for a, b in comb:
        comb2 = combinations(student-set((a, b)), 2)
        for c, d in comb2:
            comb3 = combinations(student-set((a, b, c, d)), 2)
            for e, f in comb3:
                g, h = student - set((a, b, c, d, e, f))
                temp = score(a, b, graph) + score(c, d, graph) + score(e, f, graph) + score(g, h, graph)
                ans = max(ans, temp)
    print(ans)