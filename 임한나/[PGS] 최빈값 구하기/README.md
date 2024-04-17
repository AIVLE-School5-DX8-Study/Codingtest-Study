## 최빈값 구하기
문제 링크: <https://school.programmers.co.kr/learn/courses/30/lessons/120812>

## 문제 풀이법
- 원소의 개수가 array의 최댓값인 0으로 된 리스트 my_list 생성(0이 있으므로 +1)
- for문으로 array의 숫자와 my_list 인덱스가 같을 경우, 해당 인덱스를 가진 my_list 값에 더하기 1
- my_list안의 max값의 개수 구해서 n에 저장
- n이 1이면 my_list의 max값의 인덱스 리턴, 그 외 -1 리턴