def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    for i in range(len(citations)):
        if citations[i] > h_index:
            h_index = i+1 
        else:
            break
    return h_index  
