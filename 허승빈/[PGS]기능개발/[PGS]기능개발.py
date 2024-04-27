def solution(progresses, speeds):
    dates = []
    for i in range(len(progresses)):
        days = (100-progresses[i])
        
        if days % speeds[i] ==0:
            dates.append(days // speeds[i])
        else:
            dates.append(days // speeds[i] + 1)
            
    answer = []  
    current_val = dates[0]
    count = 1
    for i in range(1,len(dates)):
        if current_val >= dates[i]:
            count += 1
        else:    
            answer.append(count)
            current_val = dates[i]
            count = 1
    answer.append(count)
            
    return answer
