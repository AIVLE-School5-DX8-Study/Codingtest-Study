def bunhae(n):
    return n + sum(int(digit) for digit in str(n))

def find_smallest(n):
    for number in range(1, n + 1):
        if bunhae(number) == n:
            return number
    return 0

N = int(input())

print(find_smallest(N))