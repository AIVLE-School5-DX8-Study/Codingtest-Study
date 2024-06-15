from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(int)
    for _, key in clothes:
        clothes_dict[key] += 1

    answer = 1
    for i in clothes_dict.values():
        answer *= (i+1)

    return answer - 1