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
