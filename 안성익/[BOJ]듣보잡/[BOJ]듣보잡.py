import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    L1 = {input().rstrip() for _ in range(N)}
    L2 = {input().rstrip() for _ in range(M)}
    L = L1.intersection(L2)
    print(len(L), *sorted(L1.intersection(L2)), sep='\n')

if __name__ == '__main__':
    main()