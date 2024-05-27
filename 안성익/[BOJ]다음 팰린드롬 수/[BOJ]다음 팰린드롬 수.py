def main() -> None:
    N = input()
    is_odd = bool(len(N) & 1)
    half_str, other_str = split_half(N, is_odd)
    if is_odd:
        if int(N) < int(half_str+half_str[-2::-1]):
            print(half_str+half_str[-2::-1])
        else:
            front_str = str(int(half_str)+1)
            back_str = front_str[-2::-1]
            result = front_str + back_str
            print(result if (len(result) - len(N)) < 2 else front_str[:-1]+back_str)
    else:
        if int(N) < int(half_str+half_str[::-1]):
            print(half_str+half_str[::-1])
        else:
            front_str = str(int(half_str)+1)
            back_str = front_str[::-1]
            result = front_str + back_str
            print(result if (len(result) - len(N)) < 2 else front_str[:-1]+back_str)

def split_half(target: str, is_odd: bool) -> tuple:
    if is_odd:
        divide_on = len(target)//2+1
    else:
        divide_on = len(target)//2
    half_str = target[:divide_on]
    other_part = target[divide_on:]
    return (half_str, other_part)

if __name__ == '__main__':
    main()