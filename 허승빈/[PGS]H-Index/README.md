# H_Index
# 문제 링크: [H_Index]<https://school.programmers.co.kr/learn/courses/30/lessons/42747>
# 풀이 방법
1. 리스트 역정렬
2. 인용 횟수 최대치부터 순환 
3. i번째 인용 횟수 > 인덱스 수  -> 1씩 증가  (>=로 하면 대칭이 안됨)
4. 그렇지 않을 경우 멈춤
5. 인덱스 수 반환
