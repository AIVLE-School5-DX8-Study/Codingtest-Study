def solution(clothes):
    # 1. 옷을 종류별로 구분하기
    closet = {}  # closet이라는 hashmap 생성
    for clothe, type in clothes:
        closet[type] = closet.get(type, 0) + 1  
        # key에 해당하는 value를 가져오기 위해 'HashMap.get(type, 0) + 1' 적용
        
    # 2. 입지 않는 경우를 추가하여 모든 조합 계산하기
    answer = 1
    for type in closet:   
        answer *= (closet[type] + 1) 
        # 'answer *= (hash_map[type] + 1)' => 모든 경우에 대해 안 입는 경우 존재
    
    # 3. 아무종류의 옷도 입지 않는 경우 제외하기
    return answer - 1

