import sys
input = sys.stdin.readline

def main() -> None:
    N, M = map(int, input().split())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    check = [list(map(int, input().split())) for _ in range(M)]
    
    for i in range(N):
        for j in range(1, N):
            numbers[i][j] += numbers[i][j-1]
    
    for i in range(1, N):
        for ii in range(N):
            numbers[i][ii] += numbers[i-1][ii]
                
    for chk in check:
        x1, y1, x2, y2 = map(lambda x: x-1, chk)
        x1 -= 1
        y1 -= 1
        if x1 >= 0 and y1 >= 0:
            print(numbers[x2][y2] - numbers[x2][y1] - (numbers[x1][y2] - numbers[x1][y1]))
        elif x1 >= 0 and y1 < 0:
            print(numbers[x2][y2] - numbers[x1][y2])
        elif x1 < 0 and y1 >= 0:
            print(numbers[x2][y2] - numbers[x2][y1])
        else:
            print(numbers[x2][y2])
            
if __name__ == '__main__':
    main()