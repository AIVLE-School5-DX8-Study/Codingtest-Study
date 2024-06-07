# 입력 받기
q_size, ex_amt = map(int, input().split())
ex_target = list(map(int, input().split()))

# 거리표 만들기
dist_arr = []
for i in range(ex_amt):
    # 시계방향으로 회전하는 경우 필요한 회전수
    clock_wise = ex_target[i] - 1
    # 반시계방향으로 회전하는 경우 필요한 회전수
    reverse_wise = q_size - clock_wise
    # 둘 중 회전수가 적은 것으로 게또
    dist_arr.append(min(clock_wise, reverse_wise))
    # 한 놈이 빠졌으니 q_size와 타겟의 인덱스에 변화가 온다.
    # 이 때 타겟의 인덱스는 새로 만들어진 큐에서의 위치를 기준으로 한다.
    q_size -= 1
    for j in range(i+1, ex_amt):
        if ex_target[i] < ex_target[j]:
            ex_target[j] -= ex_target[i]
        else:
            ex_target[j] = q_size - (ex_target[i]-ex_target[j]) + 1

# 이제 구해진 거리(회전수)를 합산
sum = 0
for d in dist_arr:
    sum += d

print(sum)
