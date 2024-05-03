## [BOJ]행렬덧셈

### 문제

N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

### 입력정보
1. 첫째 줄에 행렬의 크기 N 과 M이 주어진다.
2. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다.
3. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

### 출력정보

첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

### 풀이방법
- 행의 개수만큼 반복해서 리스트를 입력받아 행렬 만들기
- 중첩 반복문을 사용해서 [i][j]번째 원소끼리 더하기

### 코드설명
```
# 행렬의 크기
N, M = map(int, input().split())

# 행렬 A 입력 받기
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

# 행렬 B 입력 받기
B = []
for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# 행렬 덧셈
result = []
for i in range(N):
    temp = []
    for j in range(M):
        temp.append(A[i][j] + B[i][j])
    result.append(temp)

# 결과 출력
for row in result:
    print(*row)

```