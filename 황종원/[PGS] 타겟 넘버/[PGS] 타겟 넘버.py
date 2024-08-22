def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    for num in numbers:
        temp = []
        for i in leaves:
            temp.append(i + num)
            temp.append(i - num)
        leaves = temp
    
    for j in leaves:
        if j == target:
            answer += 1
            
    return answer
