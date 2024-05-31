def solution(numbers, target):
    n = len(numbers)
    return dfs(numbers, target, n)

def dfs(numbers, target, n, current_loc=0, current_sum=0):
    if current_loc == n:
        if current_sum == target:
            return 1
        else:
            return 0
    return dfs(numbers, target, n, current_loc+1, current_sum+numbers[current_loc])+\
           dfs(numbers, target, n, current_loc+1, current_sum-numbers[current_loc])