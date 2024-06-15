def solution(n, computers):
    parents = list(range(n))
    for current, computer in enumerate(computers):
        for node, connect in enumerate(computer):
            if current == node:
                continue
            if connect:
                union(parents, current, node)
                
    for i in range(n):
        parents[i] = find(parents, i)

    return len(set(parents))

def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b