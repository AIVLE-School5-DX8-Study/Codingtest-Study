from collections import deque  # deque 라이브러리 임포트
def solution(people, limit):
    count = 0
    people.sort()
    q = deque(people)
    
    while len(q) > 1: 
        if q[0] + q[-1] > limit: # 제일 가벼운 인원, 무거운 인원 합이 제한보다 크면
            q.pop()  # 제일 무거운 인원 제거
            count += 1
        else:  # 제한보다 작음 = 2명 태우기 가능
            q.popleft() # 제일 가벼운 인원 제거
            q.pop()  # 제일무거운 인원 제거
            count += 1
            
    count += len(q)  # 처음 경우로 인해 한명 남을 시      
    return count