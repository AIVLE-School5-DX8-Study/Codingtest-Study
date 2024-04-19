import sys
from itertools import permutations
N = int(sys.stdin.readline())
lst = sorted(list(sys.stdin.readline().split()), reverse=True)
if N == 1 and (lst.count('0') == 1):
    sys.stdout.write('0')
    exit()
elif lst.count('0') < 2:
    sys.stdout.write('-1')
    exit()
elif not (set(lst) - set(['0'])):
    sys.stdout.write('-1')
    exit()
    
lst.pop()
lst.pop()

perm = permutations(lst, N-2)
for nums in perm:
    s = ''
    if nums[0] == '0':
        break
    for si in nums:
        s += si
    if not (int(s)%3):
        sys.stdout.write(f'{s}00')
        exit()
sys.stdout.write('-1')