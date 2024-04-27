operators_map = ['+', '-', '*', '/']

# 가능한 모든 수식을 생성
def generate_expressions(numbers, operators, depth, expression, results):
    if depth == len(numbers) - 1:
        results.append(calculate(expression))
        return

    for i, op_count in enumerate(operators):
        if op_count > 0:
            operators[i] -= 1
            generate_expressions(numbers, operators, depth + 1, expression + [operators_map[i], numbers[depth + 1]], results)
            operators[i] += 1

# 생성된 수식을 계산하는 함수
def calculate(expression):
    result = expression[0]
    for i in range(1, len(expression), 2):
        operator = expression[i]
        operand = expression[i + 1]
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            if result < 0:
                result = -((-result) // operand)
            else:
                result //= operand
    return result




N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

results = []

generate_expressions(numbers, operators, 0, [numbers[0]], results)

print(max(results))
print(min(results))
