t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d_square = (x2-x1)**2 + (y2-y1)**2
    sum_square = (r1+r2)**2
    dif_square = (r2-r1)**2
    if  d_square > sum_square:
        print(0)
    elif d_square < dif_square:
        print(0)
    elif d_square == dif_square:
        if r1 == r2 :
            print(-1)
        else:
            print (1)
    elif d_square == sum_square:
        print(1)
    elif d_square < sum_square:
        print(2)