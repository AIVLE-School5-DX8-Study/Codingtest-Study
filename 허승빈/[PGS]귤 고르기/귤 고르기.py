def solution(k, tangerine):
    answer = 0
    num_type = {}
    for i in tangerine:
        if i in num_type:
            num_type[i] += 1
        else:
            num_type[i] = 1

    sort_num_type = sorted(num_type.values(), reverse=True)
    
    total_count = 0
    for count in sort_num_type:
        total_count += count
        answer += 1
        if total_count >= k:
            break
    return answer
