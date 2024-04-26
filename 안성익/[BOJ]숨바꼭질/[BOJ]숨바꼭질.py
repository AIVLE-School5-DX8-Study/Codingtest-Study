import sys
from collections import deque

def main():
    N, K = map(int, sys.stdin.readline().split())
    print(bfs(N, K))

def bfs(N, K):
    not_visited = [True] * 100_001
    not_visited[N] = False
    queue = deque([(N, 0)])
    
    while queue:
        position, time = queue.popleft()
        
        if position == K:
            return time
        
        next_position = (position-1, position+1, position*2)
        for nxt_pos in next_position:
            if (0 <= nxt_pos <= 100_000) and not_visited[nxt_pos]:
                not_visited[nxt_pos] = False
                queue.append((nxt_pos, time+1))

if __name__ == '__main__':
    main()