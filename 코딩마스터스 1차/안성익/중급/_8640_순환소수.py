import sys
p, q = map(int, sys.stdin.readline().split())
ans = str(p//q) + '.'
r = p%q * 10
r_lst = []
quo = []

while True:
    if str(r) in r_lst:
        break
    r_lst.append(str(r))
    quo.append(str(r//q))
    r = (r%q) * 10

repeat_idx = r_lst.index(str(r))
non_repeat = quo[:repeat_idx]
repeat = quo[repeat_idx:]

ans += ''.join(non_repeat) + "{" + ''.join(repeat) + "}"
print(ans if ans[-3:]!='{0}' else ans[:-3])