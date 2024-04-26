def main():
    X = int(input())
    dp = [0]*10000000
    for i in range(2, X+1):
        dp[i] = dp[i-1] + 1
        if not i & 1:
            dp[i] = min(dp[i], dp[i//2]+1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)
    print(dp[X])
    
if __name__ == '__main__':
    main()