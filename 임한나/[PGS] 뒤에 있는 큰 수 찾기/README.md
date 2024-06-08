## 뒤에 있는 큰 수 찾기
문제 링크: <https://school.programmers.co.kr/learn/courses/30/lessons/154539>

## 문제 풀이법
- 정답을 기록하는 answer에 numbers의 길이만큼 -1값 입력한다.
- numbers를 순회할 때 stack을 이용하여 순회, numbers[i]보다 작고, stack에 index가 기록되어 있는 배열들은 numbers[i]로 기록한다.

