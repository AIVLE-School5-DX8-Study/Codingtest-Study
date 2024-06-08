# 프로세스
# 문제 링크: [프로세스]<https://school.programmers.co.kr/learn/courses/30/lessons/42587>
# 풀이 방법
1. 리스트 컴프리헨션, enumerate함수 사용해 priorities의 원소, 인덱스를 deque로 변환
2. 큐에 처리할 프로세스 있으면, 큐의 맨앞에서 프로세스 하나 꺼냄
3. any 함수를 사용해 큐에 남아있는 다른 프로세스들과 비교해서 우선순위 낮으면 해당 프로세스를 큐 끝에 추가
4. 꺼낸 프로세스 우선순위가 큐에 남은 다른 프로세스 보다 이상이면 answer 1증가, 그리고 찾고잇는 location이면, answer반환
5. 찾을때 까지 반복
