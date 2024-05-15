# 입력 받기
q_size, ex_amt = map(int, input().split())
ex_target = list(map(int, input().split()))

# 거리표 만들기
dist_arr = []
for i in range(ex_amt):
    clock_wise = ex_target[i] - 1
    reverse_wise = q_size - clock_wise
    dist_arr.append(min(clock_wise, reverse_wise))
    # 한 놈이 빠졌으니 q_size와 타겟의 인덱스에 변화가 온다.
    q_size -= 1
    for j in range(i+1, ex_amt):
        if ex_target[i] < ex_target[j]:
            ex_target[j] -= ex_target[i]
        else:
            ex_target[j] = q_size - (ex_target[i]-ex_target[j]) + 1

sum = 0
for d in dist_arr:
    sum += d

print(sum)
