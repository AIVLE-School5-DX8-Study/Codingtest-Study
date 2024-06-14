def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = -30_001
    cnt = 0
    for start, end in routes:
        if start > camera:
            cnt += 1
            camera = end
    return cnt