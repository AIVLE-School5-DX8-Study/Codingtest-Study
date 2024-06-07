import sys
from collections import deque
input = sys.stdin.readline

def main() -> None:
    T = int(input())
    for _ in range(T):
        commands = input().rstrip()
        N = int(input())
        if N:
            x = deque(list(map(int, input()[1:-2].split(','))))
        else:
            input()
            x = []
        solution(x, commands)

def solution(x: list, commands: list) -> None:
    reversed = False
    for command in commands:
        if command == 'R':
            reversed = not reversed
        elif command == 'D':
            if x and reversed:
                x.pop()
            elif x:
                x.popleft()
            else:
                print('error')
                return
    x = list(x)
    if reversed:
        x = x[::-1]
    sys.stdout.write('[')
    print(*x, sep=',', end='')
    sys.stdout.write(']\n')
    
if __name__ == '__main__':
    main()