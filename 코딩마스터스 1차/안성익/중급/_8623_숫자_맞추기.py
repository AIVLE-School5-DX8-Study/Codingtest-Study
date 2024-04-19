from collections import deque

N, K = map(int, input().split())
queue = deque([(K, 0)])
visited = set()
visited.add(K)

while queue:
    num, cnt = queue.popleft()
    if num == N:
        break
    enable_nums = [num + 1, num - 1, num * 2]
    for num in enable_nums:
        if 0 <= num <= 100000:
            if num not in visited:
                queue.append((num, cnt + 1))
                visited.add(num)

print(cnt)