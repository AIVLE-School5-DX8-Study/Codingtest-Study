N = int(input())
x = [[] for _ in range(N)]
x[0]+=[1, 1, 1]
for i in range(1, N):
    x[i].append(sum(x[i-1]))
    x[i].append(x[i-1][0]+x[i-1][1])
    x[i].append(x[i-1][0]+x[i-1][1])
print(sum(x[N-1])%796796)