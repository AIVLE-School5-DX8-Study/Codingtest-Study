import sys
from collections import deque

def main() -> None:
    N, _ = map(int, sys.stdin.readline().split())
    deq = deque(range(1, N+1))
    nums = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for num in nums:
        idx = deq.index(num)
        if idx <= len(deq) - idx:
            ans += idx
            deq.rotate(-idx)
            deq.popleft()
        else:
            ans += len(deq)-idx
            deq.rotate(len(deq)-idx)
            deq.popleft()
    print(ans)

if __name__ == '__main__':
    main()