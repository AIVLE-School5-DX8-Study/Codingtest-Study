import sys
def find_parent(parent:list, x:int) -> int:
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent:list, a:int, b:int) -> None:
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, sys.stdin.readline().split())
parent = [0]*(N+1)

for i in range(N+1):
    parent[i] = i

edges = []
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))

ans = 0
edges.sort()
for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ans += cost

print(ans)