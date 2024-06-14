## [BOJ] 숨바꼭질

### 문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.


### 입력정보

첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

### 출력정보

수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

### 풀이방법

1. 큐를 이용하여 현재 위치와 이동 시간을 저장
2. 시작 위치를 큐에 넣고, 해당 위치를 방문 표시
3. 큐에서 현재 위치를 꺼내서 세 가지 가능한 이동(현재 위치 + 1, 현재 위치 - 1, 현재 위치 * 2)을 계산
4. 각 이동에 대해 유효한 위치이고 아직 방문하지 않은 위치라면 큐에 넣고 방문 표시
5. 이동이 동생의 위치와 일치하면 그때의 시간을 출력

### 코드설명
```
from collections import deque

def find_fastest_time(N, K):
    # 방문 여부를 체크하기 위한 배열
    visited = [False] * 100001
    
    # BFS를 위한 큐 초기화, (현재 위치, 현재 시간) 저장
    queue = deque([(N, 0)])
    visited[N] = True
    
    while queue:
        current, time = queue.popleft()
        
        # 현재 위치가 동생의 위치와 같으면 현재 시간을 반환
        if current == K:
            return time
        
        # 세 가지 이동에 대해 검사
        for next_pos in (current - 1, current + 1, 2 * current):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

# 입력 받기
N, K = map(int, input().split())
# 결과 출력
print(find_fastest_time(N, K))

```