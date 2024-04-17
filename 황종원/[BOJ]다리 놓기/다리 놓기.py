import math

def build_bridge(N, M):
    count = math.factorial(M) // (math.factorial(N) * math.factorial(M - N))
    return count

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    result = build_bridge(N, M)
    print(result)
    
