def is_possible_channel(channel, broken_buttons):
    channel_str = str(channel)
    for char in channel_str:
        if char in broken_buttons:
            return False
    return True

def min_button_presses(target_channel, broken_buttons):
    broken_buttons = set(map(str, broken_buttons))
    min_presses = abs(target_channel - 100)

    for channel in range(1000000):
        if is_possible_channel(channel, broken_buttons):
            presses = len(str(channel)) + abs(target_channel - channel)
            min_presses = min(min_presses, presses)

    return min_presses

# 입력 처리
N = int(input())
M = int(input())
if M > 0:
    broken_buttons = list(map(int, input().split()))
else:
    broken_buttons = []

print(min_button_presses(N, broken_buttons))