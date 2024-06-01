import heapq

def solution(jobs):
    jobs.sort(reverse=True)
    n = len(jobs)
    q = []
    spends = []
    now = 0
    while len(spends) != n:
        while jobs and now >= jobs[-1][0]:
            start, spend = jobs.pop()
            heapq.heappush(q, (spend, start))
        if not q:
            start, spend = jobs.pop()
            now = start
            heapq.heappush(q, (spend, start))
        spend, start = heapq.heappop(q)
        now += spend
        spends.append(now-start)
        
    return sum(spends) // n