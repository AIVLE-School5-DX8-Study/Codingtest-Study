from collections import deque

def find_fastest_time(N, K):
    visited = [False] * 100001
    queue = deque([(N, 0)])
    visited[N] = True
    
    while queue:
        current, time = queue.popleft()
        
        if current == K:
            return time
        
        for next_pos in (current - 1, current + 1, 2 * current):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

N, K = map(int, input().split())

print(find_fastest_time(N, K))
