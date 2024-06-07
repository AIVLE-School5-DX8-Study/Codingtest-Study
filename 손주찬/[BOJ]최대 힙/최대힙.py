import heapq
import sys

N = int(input())
commands = [int(sys.stdin.readline().strip()) for _ in range(N)]

heap = []

for command in commands:
    if command == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -command)
