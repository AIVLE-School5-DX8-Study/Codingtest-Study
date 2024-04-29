N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]

count = 0

for x in range(N-1, -1, -1):
    if K==0:
        break
    count += K // coins[x]
    K %= coins[x]

print(count)