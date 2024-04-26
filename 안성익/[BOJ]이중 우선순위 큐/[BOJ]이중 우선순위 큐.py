import sys
import heapq
from collections import defaultdict

def main():
    T = int(sys.stdin.readline())
    result = []
    for i in range(T):
        N = int(sys.stdin.readline())
        max_heap, min_heap = [], []
        share_heap = defaultdict(int)

        for _ in range(N):
            command, num = sys.stdin.readline().split()
            num = int(num)
            if command == 'I':
                heapq.heappush(max_heap, -num)
                heapq.heappush(min_heap, num)
                share_heap[num] += 1
            
            elif share_heap:
                temp = float('inf')
                if num==1:
                    while temp not in share_heap and max_heap:
                        temp = -heapq.heappop(max_heap)
                        if temp in share_heap:
                            share_heap[temp] -= 1
                            if share_heap[temp]==0:
                                del share_heap[temp]
                            break

                else:
                    while temp not in share_heap and min_heap:
                        temp = heapq.heappop(min_heap)
                        if temp in share_heap:
                            share_heap[temp] -= 1
                            if share_heap[temp]==0:
                                del share_heap[temp]
                            break

        result.append(share_heap)

    for heap in result:
        heap = heap.keys()
        if heap:
            print(f'{max(heap)} {min(heap)}')
        else:
            print('EMPTY')

if __name__ =='__main__':
    main()