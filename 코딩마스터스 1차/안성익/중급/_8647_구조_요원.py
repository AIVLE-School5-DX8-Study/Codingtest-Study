N = int(input())
x, y = map(int, input().split())
min_t = float('inf')
for i in range(-100, 101):
    t = pow(N*N+i*i, 0.5) + 2*pow((x-i)*(x-i)+y*y, 0.5)
    if t < min_t:
        ans = i
        min_t = t
print(ans)