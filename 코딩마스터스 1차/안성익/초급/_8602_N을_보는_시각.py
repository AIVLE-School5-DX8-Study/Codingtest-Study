import sys
N = int(sys.stdin.readline().rstrip())
h = []
m = []
s = []
sec = {i:0 for i in range(10)}
for i in range(24):
    for j in range(60):
        for k in range(60):
            s = '{:02}'.format(i)+'{:02}'.format(j)+'{:02}'.format(k)
            for ii in range(10):
                if str(ii) in s:
                    sec[ii] += 1
print(sec[N])