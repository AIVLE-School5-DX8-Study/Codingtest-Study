nTestCase = int(input())

for n in range(nTestCase):
    fib_n = int(input())

    if fib_n >= 2:
        call_count_arr = [0] * fib_n + [1]
        for i in reversed(range(2, fib_n+1)):
            call_count_arr[i-1] += call_count_arr[i]
            call_count_arr[i-2] += call_count_arr[i]

        print(call_count_arr[0], call_count_arr[1])
    elif fib_n == 1:
        print(0, 1)
    else:
        print(1, 0)
