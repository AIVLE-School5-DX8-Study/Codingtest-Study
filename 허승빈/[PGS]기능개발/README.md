## 기능 개발
문제 링크: <https://school.programmers.co.kr/learn/courses/30/lessons/42586>

## 문제 풀이법
- progresses(진도율)와 speeds(개발 속도)를 이용해서 기능별 작업 완료 기간 구하기(list)
    - if문 이용
        - (100% - 진도율) 값을 개발 속도로 나누었을 때 나머지 O : 몫 + 1
        - (100% - 진도율) 값을 개발 속도로 나누었을 때 나머지 X : 몫
- 인덱스 0일때 작업 완료 기간보다 작은 기간이면 count +=1
- 그렇지 않으면 answer 리스트에 count넣고 인덱스 갱신 , count 1로 리셋 -> answer에 카운트 담아 출력
