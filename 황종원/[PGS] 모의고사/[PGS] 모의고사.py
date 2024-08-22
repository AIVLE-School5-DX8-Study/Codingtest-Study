def solution(answers):
    man1 = [1, 2, 3, 4, 5]
    man2 = [2, 1, 2, 3, 2, 4, 2, 5]
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    answer = []
    score = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == man1[i % len(man1)]:
            score[0] += 1
        if answers[i] == man2[i % len(man2)]:
            score[1] += 1
        if answers[i] == man3[i % len(man3)]:
            score[2] += 1
            
    for j in range(len(score)):
        if score[j] == max(score):
            answer.append(j + 1)
            
    return answer

