def solution(triangle):
    num = len(triangle)
    d = [[0] * num for _ in range(num)]
    d[0][0] = triangle[0][0]

    for i in range(1, num):
        for j in range(i+1):
            if j == 0:
                # 왼쪽 끝의 경우
                d[i][j] = d[i-1][j] + triangle[i][j]
            elif j == i:
                # 오른쪽 끝의 경우
                d[i][j] = d[i-1][j-1] + triangle[i][j]
            else:
                # 중간에 위치한 값의 경우
                d[i][j] = max(d[i-1][j-1], d[i-1][j]) + triangle[i][j]
    
    return max(d[-1])
    
