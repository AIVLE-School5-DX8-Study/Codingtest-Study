from collections import Counter

def is_input_vaild() -> bool:
    counter = Counter(instr)
    for i in range(N):
        for j in range(M):
            if drawing[i][j] in counter.keys():
                counter[drawing[i][j]] -= 1

    return sum(counter.values()) == 0

def find_chr() -> set:
    chr_set = set()
    for x in range(N):
        for y in range(M):
            if drawing[x][y] != '.':
                chr_set.add((x, y))
    return chr_set

def dfs(x:int, y:int, index:int, visited:list) -> bool:
    if index == len(instr):
        return True
    
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    
    if visited[x][y] or drawing[x][y] != instr[index]:
        return False
    
    visited[x][y] = 1
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    
    for i in range(4):
        if dfs(x + dx[i], y + dy[i], index + 1, visited):
            return True
    
    visited[x][y] = 0
    return False

def count_drawings() -> int:
    ans = 0
    for x, y in chrs_idx:
        visited = [[1]*M for _ in range(N)]
        for i, j in chrs_idx:
            visited[i][j] = 0
        if dfs(x, y, 0, visited):
            ans += 1
    return ans
        
instr = input()
N, M = map(int, input().split())
drawing = [list(input()) for _ in range(N)]

if not is_input_vaild():
    print(0)
    exit()

chrs_idx = find_chr()

print(count_drawings())