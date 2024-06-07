# 자연수 n을 입력받는다.
n = int(input())

# 변환 후의 수가 저장될 문자열
new_n = ''
power = 0
while True:
    # n가 변화 후에 몇 자리수를 가질 지를 찾는다
    if 3 * (1 - 3 ** power) // -2 < n <= 3 * (1 - 3 ** (power + 1)) // -2:
        # n이 해당 자릿수를 가지는 숫자들 중에서 몇 번째인지를 구한다.
        n -= 3 * (1 - 3 ** power) // -2 - 1
        # n을 3으로 나누어 나온 값으로 가장 마지막 자릿수를 구하고, 그 나머지를 다시 n에서 뺀다.
        # 이후 n이 0이 될 때까지 해당 작업을 반복하면, 최종 변환 문자열이 나온다.
        while n:
            tmp = n % 3
            if tmp == 0:
                new_n = '4' + new_n
            elif tmp == 1:
                new_n = '1' + new_n
            else:
                new_n = '2' + new_n
            
            if tmp == 0:
                n -= 3
            else:
                n -= tmp
        
        break
    else:
        power += 1

print(new_n)