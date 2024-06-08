def solution(n):
    answer = 0
    number_of_cases = [1, 3]
    for i in range(2, n//2+1):
        number_of_cases.append((number_of_cases[i-1]*3 + sum(number_of_cases[:i-1])*2)%1000000007)
    answer = number_of_cases[n//2]
    return answer