import sys
from math import pow
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        ans = 0
        x1, y1, x2, y2 = map(int, input().split())
        N = int(input())
        for _ in range(N):
            cx, cy, r = map(int, input().split())
            ans += is_out_circle(x1, y1, cx, cy, r) ^ is_out_circle(x2, y2, cx, cy, r)
        print(ans)

def is_out_circle(x, y, cx, cy, r):
    if pow(x-cx, 2)+pow(y-cy, 2) > pow(r, 2):
        return True
    return False

if __name__ == '__main__':
    main()