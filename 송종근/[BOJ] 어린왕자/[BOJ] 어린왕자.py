test_case_amount = int(input())

while test_case_amount > 0:

    answer = 0

    start_x, start_y, end_x, end_y = map(int, input().split())
    system_amount = int(input())

    for i in range(system_amount):
        system_x, system_y, system_r = map(int, input().split())

        if ((system_x-start_x)**2 + (system_y-start_y)**2 < system_r**2) != ((system_x-end_x)**2 + (system_y-end_y)**2 < system_r**2):
            answer += 1

    print(answer)

    test_case_amount -= 1