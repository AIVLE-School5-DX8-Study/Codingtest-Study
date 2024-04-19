import sys

def is_not_bi_graph(V:list, who:int, room:list)->bool:
    stack = [who]
    room[who] = 1
    
    while stack:
        check_person = stack.pop()
        for friend in V[check_person]:
            if room[friend]==-1:
                room[friend] = 1-room[check_person]
                stack.append(friend)
            elif room[check_person] == room[friend]:
                return True
    return False

N, M = map(int, sys.stdin.readline().split())
V = {i:[] for i in range(N)}

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    V[i-1].append(j-1)
    V[j-1].append(i-1)

room = [-1]*N
for i in range(N):
    if room[i] == -1:
        if is_not_bi_graph(V, i, room):
            print(0)
            exit()
print(1)