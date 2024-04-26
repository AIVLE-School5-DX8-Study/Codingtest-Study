# function
def zero_stack(K, numbers):
    stack = []
    for num in numbers:
        if num == 0:
            stack.pop()
        else:
            stack.append(num)
    return sum(stack)

# input
K = int(input())
numbers = [int(input()) for _ in range(K)]

# result
print(zero_stack(K, numbers))