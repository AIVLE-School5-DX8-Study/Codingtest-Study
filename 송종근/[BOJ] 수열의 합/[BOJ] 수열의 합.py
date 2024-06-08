n, l = map(int, input().split())

while True:
    if 100 < l:
        print(-1)
        break
    first_value = ((2 * n / l) + 1 - l) / 2
    if 0 <= first_value:
        if first_value == int(first_value):
            first_value = int(first_value)
            for i in range(l):
                print(first_value + i)

            break
        else:
            l += 1
    else:
        l += 1