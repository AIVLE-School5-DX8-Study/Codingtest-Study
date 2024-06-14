from itertools import cycle

def solution(answers):
    p1 = cycle([1, 2, 3, 4, 5])
    p2 = cycle([2, 1, 2, 3, 2, 4, 2, 5])
    p3 = cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    cnt = [0, 0, 0]
    for answer in answers:
        if next(p1) == answer:
            cnt[0] += 1
        if next(p2) == answer:
            cnt[1] += 1
        if next(p3) == answer:
            cnt[2] += 1
    max_cnt = max(cnt)
    return [p for p in range(1, 4) if cnt[p-1]==max_cnt]