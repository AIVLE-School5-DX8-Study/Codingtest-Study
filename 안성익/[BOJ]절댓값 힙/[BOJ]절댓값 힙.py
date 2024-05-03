import sys
import heapq

def main() -> None:
    heap = []
    N = int(sys.stdin.readline())
    for _ in range(N):
        num = int(sys.stdin.readline())
        if num:
            heapq.heappush(heap, (abs(num), num))
        else:
            if heap:
                _, num = heapq.heappop(heap)
                print(num)
            else:
                print(0)

if __name__ == '__main__':
    main()