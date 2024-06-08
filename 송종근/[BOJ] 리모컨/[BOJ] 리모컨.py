# 입력 받기
chanel_number = input()
number_of_broken = int(input())
if 0 < number_of_broken:
    broken_buttons = list(input().split())

# 사용가능한 버튼
available_buttons = '0123456789'
if 0 < number_of_broken:
    for b in available_buttons:
        if b in broken_buttons:
            available_buttons = available_buttons.replace(b, '')

# 망가진 버튼의 수가 0인 경우와 10인 경우와 그 외의 경우를 분리하여 처리
if number_of_broken == 0:
    print(len(chanel_number))
elif number_of_broken == 10:
    print(abs(int(chanel_number) - 100))
else:
    closest_upper = ''
    closest_lower = ''
    
    for i in range(len(chanel_number)):
        # 숫자 버튼을 눌러서 만들 수 있는 같거나 큰 수 중에 가장 가까운 수
        if (chanel_number[i] in available_buttons
        and chanel_number[i+1:] <= max(available_buttons) * (len(chanel_number) - (i + 1))):
            closest_upper += chanel_number[i]
        else:
            for b in available_buttons:
                if chanel_number[i] < b:
                    closest_upper += b + min(available_buttons) * (len(chanel_number) - (i + 1))
                    break
            if closest_upper == '' and len(chanel_number) < 6:
                if available_buttons.replace('0', ''):
                    closest_upper = min(available_buttons.replace('0', '')) * (len(chanel_number) + 1)
            break

    for i in range(len(chanel_number)):
        # 숫자 버튼을 눌러서 만들 수 있는 작은 수 중에 가장 가까운 수
        if (chanel_number[i] in available_buttons
        and chanel_number[i+1:] > min(available_buttons) * (len(chanel_number) - (i + 1))):
            closest_lower += chanel_number[i]
        else:
            for b in reversed(available_buttons):
                if chanel_number[i] > b:
                    closest_lower += b + max(available_buttons) * (len(chanel_number) - (i + 1))
                    break
            if closest_lower == '' and len(chanel_number) > 1:
                closest_lower = max(available_buttons) * (len(chanel_number) - 1)
            if closest_lower != '':
                if int(closest_lower) == 0:
                    closest_lower = '0'
                else:
                    closest_lower = closest_lower.lstrip('0')
            break

    # 100에서 움직이는 경우, upper에서 움직이는 경우, lower에서 움직이는 경우 비교
    if closest_upper == '' and closest_lower == '':
        print(abs(int(chanel_number) - 100))
    elif closest_lower == '':
        print(min(abs(int(chanel_number) - 100), len(closest_upper) + int(closest_upper) - int(chanel_number)))
    elif closest_upper == '':
        print(min(abs(int(chanel_number) - 100), len(closest_lower) + int(chanel_number) - int(closest_lower)))
    else:
        print(min(abs(int(chanel_number) - 100), len(closest_upper) + int(closest_upper) - int(chanel_number), len(closest_lower) + int(chanel_number) - int(closest_lower)))