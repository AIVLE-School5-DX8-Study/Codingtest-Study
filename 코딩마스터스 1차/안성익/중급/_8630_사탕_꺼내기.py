import sys
from collections import deque
def rotate_direction(candy:deque, wish_number:int)->int:
    left = candy.index(wish_number)
    right = len(candy)-left
    if left <= right:
        return -left
    else:
        return right
N, M = map(int, sys.stdin.readline().split())
candy = deque(list(range(1, N+1)))
wish = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in wish:
    r = rotate_direction(candy, i)
    cnt += abs(r)
    candy.rotate(r)
    candy.popleft()
print(cnt)