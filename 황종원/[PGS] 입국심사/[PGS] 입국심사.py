def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) * n
    # right는 가장 비효율적으로 심사했을 때 걸리는 시간
    # 가장 긴 심사시간이 소요되는 심사관에게 n 명 모두 심사받는 경우
    
    while left <= right:
        mid = (left + right) //2
        total = 0 # total 은 모든 심사관들이 mid분 동안 심사한 사람의 수
        
        for time in times:
            total += mid // time # 해당 심사대에서 주어진 시간동안 심사 받은 수
            if total >= n:
                break # 중간에라도 이미 n명보다 많이 심사했다면 break
        
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if total >= n:
            answer = mid
            right = mid - 1
        
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
        else:
            left = mid + 1
    
    return answer
