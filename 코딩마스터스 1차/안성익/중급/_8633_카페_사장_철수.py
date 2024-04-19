import sys, heapq
def time_to_sec(time:str) -> int:
    return int(time[0:2])*3600 + int(time[3:5])*60 + int(time[6:])

input = sys.stdin.readline
schedule = {i:0 for i in range(86400)}
N, M = map(int, input().split())
q = []

for _ in range(M):
    enter, leave = input().split()
    enter = time_to_sec(enter)
    leave = time_to_sec(leave)
    heapq.heappush(q, (enter, leave))

cnt = 0
ans = 0
for _ in range(M):
    enter, leave = heapq.heappop(q)
    if schedule[enter] < N:
        ans += 1
        for i in range(enter, leave+1):
            schedule[i] += 1

print(ans)