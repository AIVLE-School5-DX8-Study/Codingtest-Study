import sys
input = sys.stdin.readline

def main() -> None:
    N = int(input())
    liquid = list(map(int, input().split()))
    distance = float('inf')
    left, right = 0, N-1
    result_left, result_right = 0, N-1
    while left < right:
        if abs(liquid[left]+liquid[right]) < distance:
            distance = abs(liquid[left]+liquid[right])
            result_left = left
            result_right = right
        if liquid[left]+liquid[right] < 0:
            left += 1
        else:
            right -= 1
    print(liquid[result_left], liquid[result_right])

if __name__ == '__main__':
    main()