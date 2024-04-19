import sys
_dict = {i:0 for i in range(1, 1001)}
_dict[1] = 1
_dict[2] = 2
def tile(w:int):
    if _dict[w]:
        return _dict[w]
    else:
        _dict[w] = tile(w-1) + tile(w-2)
        return _dict[w]%796796
sys.stdout.write(f'{tile(int(sys.stdin.readline()))}')