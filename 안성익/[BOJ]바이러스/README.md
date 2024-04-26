### 바이러스
- [바이러스](https://www.acmicpc.net/problem/2606)
---
### 풀이방법
1. 노드 사이의 연결을 확인하여 서로소 집합들로 나눈 후(서로 원소가 겹치지 않는 집합), 1번이 속한 집합에서 1번을 제외한 노드 수가 얼마나 있는지 확인하는 문제.
2. 서로소 집합을 만들기위해 사용되는 함수는 2개가 존재(parent는 부모 노드를 저장한 리스트).
   1. find_parent()
      - 노드 번호가 주어졌을 때, 해당 노드가 어떤 집합에 속해 있는지 확인하는 함수
      - 재귀 호출을 통해 연결된 노드를 계속 탐색하면서, 결국 부모 노드를 만나 최종적인 parent리스트로 업데이트할 수 있음
        ``` Python
        def find_parent(parent, node):
            if parent[node] != node:
                parent[node] = find_parent(parent, parent[node])
            return parent[node]
        ``` 
   2. union_find()
      - 연결 정보를 입력받아 부모 노드의 집합에 노드를 연결시키는 함수
      - 각각의 부모 노드를 연결함으로써 새로운 서로소 집합을 구성할 수 있게 함. 
        ``` Python
        def union_find(parent, node1, node2):
            node1 = find_parent(parent, node1)
            node2 = find_parent(parent, node2)
            if node1 != node2:
                parent[node2] = node1
        ``` 
3. M개의 연결 정보를 받은 후 서로소 집합 정보(parent)를 계속 업데이트 시키면서 서로소 집합을 만듦.
4. 1번 노드 또한 union_find에 의해 업데이트 되면서 현재 상태를 모르므로 find_parent를 이용하여 다시 최신화함.
5. 그외의 노드들에 대해서도 다시 부모 노드를 찾게함으로써 만약, 1번 노드의 서로소 집합과 일치할 경우 count하여 연결된 모든 노드 수를 확인할 수 있음.