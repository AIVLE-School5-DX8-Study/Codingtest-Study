
# 예시에 대한 부분을 역으로 구상

def solution(n):
    a = 0              # 개수 세아리기 위함 
    while n > 0:       # n > 0 면 계속 돌아감
        if n % 2 == 0: # 짝수면
            n /= 2     # 반으로 나눔
        else:          # 홀수면
            n -= 1     # 한칸 이동

            a += 1     # 한칸 이동되는 경우마다 count
    return a
    
