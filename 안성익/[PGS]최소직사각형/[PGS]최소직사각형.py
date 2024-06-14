def solution(sizes):
    max_b = float('-inf')
    max_h = float('-inf')
    for a, b in sizes:
        if a <= b:
            max_b = max(max_b, b)
            max_h = max(max_h, a)
        else:
            max_b = max(max_b, a)
            max_h = max(max_h, b)
    return max_b * max_h