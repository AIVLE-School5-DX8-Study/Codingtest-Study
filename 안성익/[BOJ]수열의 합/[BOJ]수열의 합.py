import sys

def main() -> None:
    N, L = map(int, sys.stdin.readline().split())
    d = ((L-1)*L) // 2
    for _ in range(100):
        if L > 100:
            break
        if (N - d) % L :
            L += 1
            d = ((L-1)*L) // 2
        else:
            if (N-d) < 0:
                continue
            else:
                print(*range(((N-d) // L), ((N-d) // L) + L))
                return
    print(-1)
    
if __name__ == '__main__':
    main()