import sys
from itertools import combinations

def get_IoU(rect1:list, rect2:list)->float:
    intersection_x_len = min(rect1[0]+rect1[2], rect2[0]+rect2[2]) - max(rect1[0], rect2[0])
    intersection_y_len = min(rect1[1]+rect1[3], rect2[1]+rect2[3]) - max(rect1[1], rect2[1])
    if intersection_x_len <= 0 or intersection_y_len <= 0:
        return 0
    intersection_area = intersection_x_len * intersection_y_len
    union_area = rect1[2]*rect1[3]+rect2[2]*rect2[3] - intersection_area
    return (intersection_area)/(union_area)

N = int(sys.stdin.readline())
MAT = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
comb = combinations(range(N), 2)
max_IoU = -float('inf')
for rect1, rect2 in comb:
    IoU = get_IoU(MAT[rect1], MAT[rect2])
    if IoU > max_IoU:
        max_IoU = IoU
        ans = (rect1+1, rect2+1)

print(*ans)