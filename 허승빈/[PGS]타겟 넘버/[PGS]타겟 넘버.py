def solution(numbers, target):
    suum = 0
    visits = [0]
    for i in numbers:
        ans = []
    
        for visit in visits:
            ans.append(visit-i)
            ans.append(visit+i)

        visits = ans
    for visit in visits:
        if visit == target:
            suum += 1
            
    return suum
