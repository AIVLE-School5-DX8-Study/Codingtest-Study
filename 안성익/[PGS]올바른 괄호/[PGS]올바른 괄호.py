def solution(s):
    num = 0
    for si in s:
        if si=='(':
            num += 1
        else:
            num -= 1
            if num < 0:
                return False

    return False if num else True