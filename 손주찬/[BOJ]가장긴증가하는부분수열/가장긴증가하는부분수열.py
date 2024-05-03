def long(numbers):
    n = len(numbers)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if numbers[i] > numbers[j]:
                dp[i] = max(dp[i], dp[j]+1)
    
    return max(dp)

N = int(input())
A = list(map(int, input().split()))

print(long(A))