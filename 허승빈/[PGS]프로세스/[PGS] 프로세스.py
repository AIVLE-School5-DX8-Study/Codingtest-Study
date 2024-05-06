from collections import deque
def solution(priorities, location):
    que = deque([(p, i) for i, p in enumerate(priorities)])
    answer = 0
    
    while que:
        item = que.popleft()
        if any(item[0] < other[0] for other in que):
            que.append(item)
        else:
            answer += 1
            if item[1] == location:
                return answer