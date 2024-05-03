from itertools import permutations

def solution(numbers):
    
    answer = ''.join(sorted(
        list(map(str,numbers)),
        key=lambda x : x*3,
        reverse=True
        ))

    return str(int(answer))