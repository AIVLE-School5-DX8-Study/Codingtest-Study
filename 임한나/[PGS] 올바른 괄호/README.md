## 올바른 괄호
문제 링크: <https://school.programmers.co.kr/learn/courses/30/lessons/12909>

## 문제 풀이법
- ( 이면 answer에 (를 추가한다.
- ) 일 때 answer가 비었으면 짝이 맞지 않으므로 FAlse를 return한다.
- 그렇지 않으면 즉, 짝이 맞으면 ( 를 pop으로 삭제한다.
- 짝이 맞는다면 answer안에는 ( 사라져서 빈 리스트가 되므로 True를 return한다.