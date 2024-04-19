import sys
N = int(sys.stdin.readline())
_dict = {i:[] for i in range(1, 1001)}

for _ in range(N):
    s = sys.stdin.readline().rstrip()
    if s not in _dict[len(s)]:
        _dict[len(s)].append(s)

for v in _dict.values():
    v.sort()
    for i in v:
        sys.stdout.write(f'{i}\n')