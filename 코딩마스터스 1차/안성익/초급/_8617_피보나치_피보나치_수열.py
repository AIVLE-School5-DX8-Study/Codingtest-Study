import sys
d = {1:1, 2:1, 3:2}
dd = []

def fibo(num:int):
    if num in d:
        return d[num]
    else:
        d[num] = fibo(num-1)+fibo(num-2)
        return d[num]

a, b = map(int, sys.stdin.readline().split())
fibo(10)
for k, i in d.items():
    for _ in range(i):
        dd.append(i)
sys.stdout.write(str(sum(dd[a-1:b])))