from sys import setrecursionlimit
from functools import cache

def main() -> None:
    setrecursionlimit(2000)
    print(tile(int(input())))

@cache
def tile(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return (tile(n-1) + tile(n-2))%10_007

if __name__ == '__main__':
    main()