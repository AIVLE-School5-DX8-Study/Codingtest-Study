# 입력 받기
chanel_number = input()
number_of_broken = int(input())
broken_buttons = list(input().split())

# 사용가능하나 버튼
available_buttons = [n for n in range(10) if n not in broken_buttons]

# 망가진 버튼의 수가 0인 경우와 10인 경우와 그 외의 경우를 분리하여 처리
if number_of_broken == 0:
    print(len(chanel_number))
elif number_of_broken == 10:
    print(abs(int(chanel_number) - 100))
else:
    closest_upper = ''
    closest_lower = ''
    for i in len(chanel_number):
        if chanel_number[i] in available_buttons:
            if chanel_number[i+1:] <= max(available_buttons) * (len(chanel_number) - (i + 1)):
                closest_upper += chanel_number[i]
            else:
                
        else:
            for b in available_buttons:
                if e < b:
                    closest_upper = min(closest_upper, b + min(available_buttons) * (len(chanel_number) - 1))
            