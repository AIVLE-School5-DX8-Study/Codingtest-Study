### 용액
- [용액](https://www.acmicpc.net/problem/2467)
### 풀이방법
- 이분탐색과 투 포인터를 결합한 문재.
- 만약, 이분탐색으로 계산하지 않고 단순 조합으로 풀이한다면 최악의 경우 4,999,950,000 ($_{100,000}C_{2}$)번의 반복 계산이 필요하므로, 시간 초과될 수 있어 $logN$의 시간복잡도를 갖는 이분탐색을 사용해야한다.
- 문제 풀이를 위한 로직은 다음과 같다
  1. 용액을 섞은 후 값이 음수일 경우 한 혼합액의 알칼리성이 큰 경우이므로, 좌측 포인터를 한 칸 뒤로 옮긴다.
  2. 반대로, 용액을 섞은 후 값이 양수 일 경우 혼합액의 산성이 큰 경우이므로, 우측 포인터를 한 칸 앞으로 옮긴다.
  3. 기존 값보다 작아 최솟값을 갱신할 수 있는 경우 최솟값을 갱신하고 해당 시점의 포인터들(인덱스)을 저장할 수 있도록 한다.
  4. 포인터가 한 점으로 모일 때 까지 1~3 과정을 반복한다.
