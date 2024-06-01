## [BOJ] 리모컨

### 문제
수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.

리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.

수빈이가 지금 보고 있는 채널은 100번이다.


### 입력정보
1. 첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.
2. 둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다.
3. 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.

### 출력정보

첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.

### 풀이방법
1. 접근 방식
    1. 현재 채널이 100이므로, 기본적으로 +와 - 버튼을 눌러서 목표 채널 N에 도달하는 방법을 고려
    2. 고장난 숫자 버튼을 피하는 방법 파악. <br> 즉, 고장나지 않은 숫자 버튼을 이용해 채널 N에 최대한 가까운 숫자를 직접 입력한 후, +와 - 버튼을 사용하는 방법
2. 구현 전략
    1. 주어진 목표 채널 N에서 현재 채널 100까지의 단순한 +와 - 버튼을 사용하는 경우를 고려하여 기본적인 버튼 누름 횟수를 계산
    2. 모든 가능한 채널 번호를 확인하면서, 그 번호가 고장난 버튼을 사용하지 않고 입력 가능한지 확인
    3. 입력 가능한 가장 가까운 채널을 찾아, 그 채널로 이동 후 +와 - 버튼을 사용하여 목표 채널 N에 도달하는 방법을 계산

### 코드설명
```
def is_possible_channel(channel, broken_buttons):
    # 주어진 채널 번호를 문자열로 변환
    channel_str = str(channel)
    
    # 채널 번호의 각 자릿수를 확인
    for char in channel_str:
        # 자릿수가 고장난 버튼에 포함되어 있으면 False 반환
        if char in broken_buttons:
            return False
    # 모든 자릿수가 고장난 버튼에 포함되지 않으면 True 반환
    return True

def min_button_presses(target_channel, broken_buttons):
    # 고장난 버튼들을 문자열로 변환하여 집합으로 저장 (검색 속도 향상)
    broken_buttons = set(map(str, broken_buttons))
    
    # 기본적으로 +와 - 버튼만 사용하여 목표 채널에 도달하는 방법의 버튼 누름 횟수를 초기값으로 설정
    min_presses = abs(target_channel - 100)
    
    # 모든 가능한 채널 번호를 확인 (0부터 999,999까지 충분히 큰 수까지 시도)
    for channel in range(1000000):
        # 해당 채널 번호가 고장난 버튼을 사용하지 않고 입력 가능한지 확인
        if is_possible_channel(channel, broken_buttons):
            # 채널 번호를 입력하는 데 필요한 버튼 누름 횟수 (채널 번호의 자릿수 길이)
            presses = len(str(channel))
            # 입력한 채널 번호에서 목표 채널까지 도달하는 데 필요한 +와 - 버튼 누름 횟수
            presses += abs(target_channel - channel)
            # 최소 버튼 누름 횟수 갱신
            min_presses = min(min_presses, presses)
    
    # 계산된 최소 버튼 누름 횟수 반환
    return min_presses

# 입력 처리
N = int(input())  # 목표 채널 번호 입력
M = int(input())  # 고장난 버튼의 개수 입력
if M > 0:
    # 고장난 버튼의 목록 입력
    broken_buttons = list(map(int, input().split()))
else:
    # 고장난 버튼이 없는 경우 빈 리스트로 설정
    broken_buttons = []

# 최소 버튼 누름 횟수를 계산하여 출력
print(min_button_presses(N, broken_buttons))


```