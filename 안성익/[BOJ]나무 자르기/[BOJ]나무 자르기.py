import sys
input = sys.stdin.readline

def main() -> None:
    N, M = map(int, input().split())
    heights = list(map(int, input().split()))
    left, right = 1, max(heights)
    result = 0
    while left <= right:
        mid = (left+right)//2
        if enable(heights, mid, M):
            left = mid + 1
            result = mid
        else:
            right = mid - 1
    print(result)

def enable(heights: list, cutter_height: int, want: int) -> bool:
    result = 0
    for height in heights:
        result += max(0, height-cutter_height)
        if result >= want:
            return True
    return result >= want

if __name__ == '__main__':
    main()