number = int(input())

# 자리수 구하기
number_len = 0
number_copy = number
while number_copy:
    number_len += 1
    number_copy //= 10

final_number = 0

# 수의 중심을 기준으로 좌우 비교
# 자릿수의 경계에 있는 값인지 아닌지 우선 판별
# 경계값이라면 그냥 2 더해서 출력
# 경계값이 아니면 한자리 수와 다른 수들을 구분하여 진행
if len(str(number+1)) != len(str(number)):
    final_number = number + 2
    print(final_number)
elif number_len > 1:
    bound = number_len // 2
    # 자릿수가 홀수인 경우 그 가운데 수를 기준으로 양쪽 수를 비교
    # 왼쪽수가 오른쪽 수보다 같거나 크면 오른쪽 수를 왼쪽수를 뒤집은 것으로 대치
    # 그 외의 경우에는 왼쪽수에 1을 더하여 그것을 뒤집은 것을 오른쪽 수 자리에 대치
    if number_len % 2 == 1:
        upper_number = number // (10 ** bound)
        middle_number = upper_number % 10
        upper_number = upper_number // 10
        lower_number = number % (10 ** bound)
        reversed_upper_number = int(''.join(reversed(list(str(upper_number)))))
        if reversed_upper_number <= lower_number:
            upper_number = int(str(upper_number) + str(middle_number)) + 1
            lower_number = int(''.join(reversed(list(str(upper_number)[:-1]))))
            final_number = int(str(upper_number) + str(lower_number))
        else:
            upper_number = int(str(upper_number) + str(middle_number))
            lower_number = int(''.join(reversed(list(str(upper_number)[:-1]))))
            final_number = int(str(upper_number) + str(lower_number))
    # 자릿수가 짝수인 경우 반반으로 가르기
    # 마찬가지로 왼쪽수가 오른쪽 수보다 같거나 크면 오른쪽 수를 왼쪽수를 뒤집은 것으로 대치
    # 그 외의 경우에는 왼쪽수에 1을 더하여 그것을 뒤집은 것을 오른쪽 수 자리에 대치
    else:
        upper_number = number // (10 ** bound)
        lower_number = number % (10 ** bound)
        reversed_upper_number = int(''.join(reversed(list(str(upper_number)))))

        if reversed_upper_number <= lower_number:
            upper_number += 1
            final_number = int(str(upper_number) + ''.join(reversed(list(str(upper_number)))))
        else:
            final_number = int(str(upper_number) + ''.join(reversed(list(str(upper_number)))))
else:
    final_number = number + 1

print(final_number)