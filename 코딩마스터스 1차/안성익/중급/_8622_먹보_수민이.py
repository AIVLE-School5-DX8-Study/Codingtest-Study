import sys, heapq
input = sys.stdin.readline

N = int(input())
MAP = sorted([tuple(map(int, input().split())) for _ in range(N)])
L, P = map(int, input().split())

cur_pos = 0
ans = 0
q = []

if P >= L:
    print(0)
    exit()

for dist, food in MAP:
    if dist > L:
        break
    dist_to_store = dist - cur_pos
    while P < dist_to_store:
        if q:
            P += -heapq.heappop(q)
            ans += 1
        else:
            print(-1)
            exit()

    P -= dist_to_store
    cur_pos = dist
    heapq.heappush(q, -food)

dist_to_goal = L - cur_pos
while P < dist_to_goal:
    if q:
        P += -heapq.heappop(q)
        ans += 1
    else:
        print(-1)
        exit()

print(ans)