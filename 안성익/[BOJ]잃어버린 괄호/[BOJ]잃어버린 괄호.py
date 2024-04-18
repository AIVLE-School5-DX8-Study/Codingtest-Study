def main() -> None:
    eq = input().split('-')
    sub_eqs = map(get_sum, eq)
    ans = next(sub_eqs)
    for sub_eq in sub_eqs:
        ans -= sub_eq
    print(ans)

def get_sum(numbers: str) -> int:
    ans = sum(map(int, numbers.split('+')))
    return ans

if __name__ == '__main__':
    main()