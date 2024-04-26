## [BOJ]제로

### 문제
N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다.<br/>
또, 수와 수 사이에 끼워넣을 수 있는 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.<br/>
연산자의 개수는 N-1보다 많을 수도 있다.<br/>
모든 수의 사이에는 연산자를 한 개 끼워넣어야 하며, 주어진 연산자를 모두 사용하지 않고 모든 수의 사이에 연산자를 끼워넣을 수도 있다.<br/><br/>
우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.<br/>

예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 주어진 연산자가 덧셈(+) 3개, 뺄셈(-) 2개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 250가지의 식을 만들 수 있다. 예를 들어, 아래와 같은 식을 만들 수 있다.

- 1+2+3-4×5÷6
- 1÷2+3+4-5×6
- 1+2÷3×4-5+6
- 1÷2×3-4+5+6
- 1+2+3+4-5-6
- 1+2+3-4-5×6

식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.

- 1+2+3-4×5÷6 = 1
- 1÷2+3+4-5×6 = 12
- 1+2÷3×4-5+6 = 5
- 1÷2×3-4+5+6 = 7
- 1+2+3+4-5-6 = -1
- 1+2+3-4-5×6 = -18

<b>N개의 수와 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.</b>


### 입력정보
1. 첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다.
2. 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100)
3. 셋째 줄에는 합이 N-1보다 크거나 같고, 4N보다 작거나 같은 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 

### 출력정보
1. 첫째 줄에 만들 수 있는 식의 결과의 최댓값을 출력
2. 둘째 줄에는 최솟값을 출력
- 참고: 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.

### 풀이방법
- 브루트포스 알고리즘: 가능한 모든 경우의 수를 직접적으로 확인하면서 해답을 찾는 방법
1. 생성 가능한 모든 수식을 저장한다.
2. 그에 따른 결과를 계산해서 최댓값과 최솟값을 출력

### 코드설명
```
operators_map = ['+', '-', '*', '/']  # 연산자 종류 선언하고 시작

## 모든 가능한 수식을 생성하는 함수
def generate_expressions(numbers, operators, depth, expression, results):
    if depth == len(numbers) - 1:
        # 수식이 완성되면 계산하여 결과를 results 리스트에 추가
        results.append(calculate(expression))
        return

    # 현재 위치에서 가능한 모든 연산자를 시도
    for i, op_count in enumerate(operators):
        if op_count > 0:
            # 해당 연산자를 사용하여 다음 숫자와 결합한 수식을 생성하고 재귀 호출
            operators[i] -= 1  # 사용한 연산자 개수를 하나 줄임
            generate_expressions(numbers, operators, depth + 1, expression + [operators_map[i], numbers[depth + 1]], results)
            operators[i] += 1  # 재귀 호출이 끝나면 다시 연산자 개수를 복구

## 주어진 식을 계산하는 함수
def calculate(expression):
    # 연산자 우선순위 무시하고 앞에서부터 계산
    result = expression[0]  # 결과를 저장할 변수 초기화
    for i in range(1, len(expression), 2):
        operator = expression[i]  # 현재 연산자
        operand = expression[i + 1]  # 현재 연산자의 다음 숫자
        if operator == '+':
            result += operand  # 덧셈 연산
        elif operator == '-':
            result -= operand  # 뺄셈 연산
        elif operator == '*':
            result *= operand  # 곱셈 연산
        elif operator == '/':
            # 나눗셈은 정수 나눗셈으로 몫만 취함
            if result < 0:
                result = -((-result) // operand)
            else:
                result //= operand
    return result  # 계산된 결과 반환

# 입력 받기
N = int(input())  # 수의 개수
numbers = list(map(int, input().split()))  # 수열
operators = list(map(int, input().split()))  # 연산자 개수

results = []  # 모든 수식의 결과를 저장할 리스트

# 가능한 모든 수식 생성
generate_expressions(numbers, operators, 0, [numbers[0]], results)

# 최댓값과 최솟값 출력
print(max(results))
print(min(results))

```