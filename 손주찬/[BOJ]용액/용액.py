def find_closest_to_zero(n, solutions):
    left = 0
    right = n - 1
    closest_sum = float('inf')
    answer = (0, 0)

    while left < right:
        current_sum = solutions[left] + solutions[right]

        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            answer = (solutions[left], solutions[right])

        if current_sum > 0:
            right -= 1
        else:
            left += 1

    return answer

n = int(input())
solutions = list(map(int, input().split()))

result = find_closest_to_zero(n, solutions)
print(result[0], result[1])
