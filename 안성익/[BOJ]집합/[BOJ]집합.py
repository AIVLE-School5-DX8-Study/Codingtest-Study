import sys

def main():
    _set = set()
    set_all = {i for i in range(1, 21)}
    N = int(sys.stdin.readline())
    
    for _ in range(N):
        inp = sys.stdin.readline().split()
        if len(inp)==1:
            if inp[0] == 'all':
                _set = set_all.copy()
            else:
                _set.clear()
        else:
            if inp[0]=='add':
                _set.add(int(inp[1]))
            elif inp[0]=='remove':
                if int(inp[1]) in _set:
                    _set.remove(int(inp[1]))
            elif inp[0]=='toggle':
                if int(inp[1]) in _set:
                    _set.remove(int(inp[1]))
                else:
                    _set.add(int(inp[1]))
                    
            else:
                if int(inp[1]) in _set:
                    print(1)
                else:
                    print(0)

if __name__ == '__main__':
    main()