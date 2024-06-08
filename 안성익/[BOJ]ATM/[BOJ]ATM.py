import sys
input = sys.stdin.readline

def main():
    N = int(input())
    lst = sorted(list(map(int, input().split())))
    print(user_sum(lst))

def user_sum(lst):
    for i in range(1, len(lst)):
        lst[i] += lst[i-1]
    return sum(lst)

if __name__ == '__main__':
    main()