# 탐욕법 일고리즘

def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[1]) # routes를 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치를 찾음
    
    for route in routes:
        if camera < route[0]: 
            # 기준(카메라)보다 진입지점이 뒤에 있으면 (현재 카메라 위치로 차량을 만나지 못함)
            answer += 1 # 카메라를 추가
            camera = route[1] # 최근 카메라의 위치(route[1])를 갱신
    
    return answer