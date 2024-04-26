import sys
input = sys.stdin.readline

def main():
    N = int(input())
    M = int(input())
    parent = list(range(N+1))
    
    for _ in range(M):
        i, j = map(int, input().split())
        union_find(parent, i, j)

    parent1 = find_parent(parent, 1)
    print(sum(1 for i in range(2, N+1) if find_parent(parent, i)==parent1))

def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union_find(parent, node1, node2):
    node1 = find_parent(parent, node1)
    node2 = find_parent(parent, node2)
    if node1 != node2:
        parent[node2] = node1

if __name__ == '__main__':
    main()