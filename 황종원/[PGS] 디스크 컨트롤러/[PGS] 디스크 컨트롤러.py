import heapq

def solution(jobs):
    answer = 0
    now = 0      # 현재시간
    i = 0        # 처리개수
    start = -1   # 마지막 완료시간
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 작업을 heap에 저장
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap,[job[1],job[0]])
        
        if len(heap) > 0:   # 처리할 작업이 있는 경우 
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += now - current[1] # 요청으로부터 처리시간
            i += 1
        else:   # 처리할 작업이 없는 경우 다음 시간으로 넘어감
            now += 1
            
    return answer // len(jobs)   # 평균 시간 리턴

