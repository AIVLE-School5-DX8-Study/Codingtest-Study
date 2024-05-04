import sys

def main() -> None:
    N, M = map(int, sys.stdin.readline().split())
    graph = sorted([int(sys.stdin.readline()) for _ in range(N)])
    
    xi = 1
    xl = graph[-1] - graph[0]
    
    while xi <= xl:
        xm = (xi+xl) // 2
        if count_enable_install(graph, xm) >= M:
            ans = xm
            xi = xm + 1
        else:
            xl = xm - 1

    print(ans)

def count_enable_install(graph: list, min_dist: int) -> int:
    ans = 1
    check_point = graph[0]
    for i in range(1, len(graph)):
        if graph[i] >= check_point + min_dist:
            ans += 1
            check_point = graph[i]
            
    return ans 

if __name__ == '__main__':
    main()