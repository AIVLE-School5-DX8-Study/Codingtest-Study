import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    coins = []
    for _ in range(N):
        coin = int(input())
        if coin <= K:
            coins.append(coin)
    ans = 0
    for coin in coins[::-1]:
        temp = K // coin
        ans += temp
        K -= coin*temp
        if not K:
            break

    print(ans)

if __name__ == '__main__':
    main()