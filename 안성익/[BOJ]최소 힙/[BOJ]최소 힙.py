import sys
import heapq

def main():
    N = int(sys.stdin.readline())
    heap = []
    for _ in range(N):
        num = int(sys.stdin.readline())
        if num:
            heapq.heappush(heap, num)
        else:
            if heap:
                sys.stdout.write(f'{heapq.heappop(heap)}\n')
            else:
                sys.stdout.write('0\n')
                

if __name__ == '__main__':
    main()