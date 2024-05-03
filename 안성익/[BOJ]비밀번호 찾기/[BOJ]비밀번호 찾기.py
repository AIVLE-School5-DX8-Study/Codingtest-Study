import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    dic = {}
    for _ in range(N):
        address, password = input().split()
        dic[address] = password
    for _ in range(M):
        print(dic[input().rstrip()])

if __name__ == '__main__':
    main()