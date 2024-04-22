import sys

def main() -> None:
    N = int(sys.stdin.readline())
    time = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    time.sort()
    time.sort(key=lambda x: x[1])
    
    ans = 0
    old_time = -1

    for i, j in time:
        if i >= old_time:
            ans += 1
            old_time = j

    print(ans)

if __name__ == '__main__':
    main()