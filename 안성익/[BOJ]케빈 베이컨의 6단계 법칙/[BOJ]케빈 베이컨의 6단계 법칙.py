import sys
from collections import deque

inf = 101
def main():
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N)]
    distance = [[inf]*N for _ in range(N)]

    for i in range(N):
        distance[i][i] = 0
    
    for _ in range(M):
        i, j = map(int, sys.stdin.readline().split())
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)
        
    _min = float('inf')
    
    for i in range(N):
        number = bfs(i, graph, distance)
        if number < _min:
            ans = i
            _min=number
    
    print(ans+1)

def bfs(start, graph, distance):
    queue = deque([start])

    while queue:
        currnet_node = queue.popleft()

        for next_node in graph[currnet_node]:
            if distance[start][next_node] == inf:
                distance[start][next_node] = distance[start][currnet_node]+1
                queue.append(next_node)

    return sum(distance[start])

if __name__ == '__main__':
    main()