import sys
from collections import deque
input = sys.stdin.readline

def main() -> None:
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    solution = Solution(graph, N, M)
    print(solution.count_areas())

class Solution:
    def __init__(self, graph:list, row_len:int, column_len:int):
        self.graph = graph
        self.row_len = row_len
        self.column_len = column_len
        self.directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    def bfs(self, x:int, y:int):
        queue = deque([(x, y)])
        self.graph[y][x] = 0
        while queue:
            x, y = queue.popleft()
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.column_len and 0 <= ny < self.row_len:
                    if self.graph[ny][nx] == 1:
                        self.graph[ny][nx] = 0
                        queue.append((nx, ny))
        return 1
    
    def count_areas(self):
        result = 0
        for y in range(self.row_len):
            for x in range(self.column_len):
                if self.graph[y][x] == 1:
                    result += self.bfs(x, y)
        return result

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        main()