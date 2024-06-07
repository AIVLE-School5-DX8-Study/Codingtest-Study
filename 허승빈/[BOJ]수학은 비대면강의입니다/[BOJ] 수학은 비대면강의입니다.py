mport sys
a, b, c, d, e, f = map(int,sys.stdin.readline().split()) # 공백 분리 후 정수 변환, 여러개 분할
for x in range(-999,1000):        # 브루드포스
    for y in range(-999, 1000):
        if a*x+b*y == c and d*x+e*y == f:
            print(x, y)
            break