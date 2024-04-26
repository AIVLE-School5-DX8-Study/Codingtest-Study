import math
def solution(arr):
    for i in range(len(arr)-1):
			  # 최대 공약수
        gcd = math.gcd(arr[i], arr[i+1])
        # 최소 공배수
        lcd = (arr[i]*arr[i+1]) // gcd
        # 최소 공배수 업뎃
        arr[i+1] =lcd
    return lcd