### 다리 놓기
- 문제 링크: [다리 놓기](https://www.acmicpc.net/problem/1010)
---
### 풀이 방법
1. 다리를 선택하는 경우의 수 (순서 상관 X, 겹치지 않아야 함)
2. '조합'을 사용하여 계산
3. 동쪽의 M개와 서쪽의 N개를 연결 (N <= M) => 즉, M개 중 N개를 선택하는 경우의 수 => mCn =  M! / (N! * (M-N)!) 