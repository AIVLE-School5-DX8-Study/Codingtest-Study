## [BOJ]좌표정렬하기

### 문제
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

### 입력정보
- 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다.
- 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 
- 좌표는 항상 정수이고, 위치가 같은 두 점은 없다다.

### 출력정보
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

### 풀이방법
1.sorted() 함수에 key를 전달해서 정렬의 기준이 되는 요소 제공 

### 코드설명
```
# 입력 받기
N = int(input())
points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# x좌표를 기준으로 정렬하되, x좌표가 같으면 y좌표를 기준으로 정렬
sorted_points = sorted(points, key=lambda x: (x[0], x[1]))

# 정렬된 점 출력
for point in sorted_points:
    print(point[0], point[1])

```