N = int(input())

points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

sorted_points = sorted(points, key=lambda x: (x[0], x[1]))

for point in sorted_points:
    print(point[0], point[1])
