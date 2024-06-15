from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        words += list(product(['A', 'E', 'I', 'O', 'U'], repeat=i))
    words.sort()
    return words.index(tuple(word)) + 1