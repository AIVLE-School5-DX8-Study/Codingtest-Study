import sys
from itertools import permutations

def isValid(parts:list, puzzle:list) -> bool:
    read_by_rows = parts
    read_by_cols = list(zip(*parts))
    puzzle_set = sorted(read_by_rows + read_by_cols)
    puzzle_sorted = sorted(puzzle)
    return puzzle_set == puzzle_sorted

puzzle = [tuple(sys.stdin.readline().rstrip()) for _ in range(6)]
comb = permutations(range(6), 3)
results = []
for i, j, k in comb:
    parts = [puzzle[i], puzzle[j], puzzle[k]]
    if isValid(parts, puzzle):
        parts = list(map(list, parts))
        results.append(''.join(parts[0]) + ''.join(parts[1]) + ''.join(parts[2]))
result = sorted(results)[0]
print(result[0:3])
print(result[3:6])
print(result[6:9])